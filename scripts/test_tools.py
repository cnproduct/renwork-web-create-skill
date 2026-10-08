#!/usr/bin/env python3
"""Small runnable regression check for evidence, compiler, audit and preview boundaries."""
import contextlib
import io
import json
import subprocess
import sys
import tempfile
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
from dev_server import B2BRequestHandler
from extract_design_tokens import extract_tokens
from geo_seo_engine import generate_seo_geo_assets, SM, XHTML
from layout_typography_auditor import audit_directory, schema_shape
from site_forensics import run_forensics


def rejects(action):
    try:
        action()
    except (ValueError, OSError, KeyError, TypeError):
        return
    raise AssertionError('Invalid input was accepted')


class Fixture(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class QuietPreview(B2BRequestHandler):
    def log_message(self, *args):
        pass


def main():
    with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()):
        root = Path(tmp)
        site = root / 'site'
        site.mkdir()
        en = '<html lang="en"><head><title>A &amp; B</title><meta name="viewport" content="width=device-width"></head><body><h1>Products</h1><img src="x.svg" alt=""></body></html>'
        (site / 'index.html').write_text(en)
        (site / 'de.html').write_text(en.replace('lang="en"', 'lang="de"'))
        alternatives = {'en': '/', 'de': '/de.html'}
        config = {'domain': 'https://target.example', 'brand_name': 'A & B', 'company_name': 'Real Target', 'mode': 'release', 'generate_llms': True,
                  'pages': [{'path': '/', 'file': 'index.html', 'title': 'A & B', 'lang': 'en', 'alternates': alternatives},
                            {'path': '/de.html', 'file': 'de.html', 'title': 'Deutsch', 'lang': 'de', 'alternates': alternatives}]}
        records = generate_seo_geo_assets(config, site)
        tree = ET.parse(site / 'sitemap.xml')
        assert len(tree.findall(f'{{{SM}}}url')) == 2
        assert len(tree.findall(f'.//{{{XHTML}}}link')) == 4
        assert records[0]['schema']['@graph'][0]['name'] == 'Real Target'
        assert 'xhplasticlife' not in (site / 'llms.txt').read_text()
        old = (site / 'robots.txt').read_bytes()
        rejects(lambda: generate_seo_geo_assets(config, site))
        assert (site / 'robots.txt').read_bytes() == old
        bad = json.loads(json.dumps(config))
        bad['pages'][1]['alternates'] = {}
        rejects(lambda: generate_seo_geo_assets(bad, site, True))
        bad = json.loads(json.dumps(config))
        bad['pages'][0]['file'] = '../outside.html'
        (root / 'outside.html').write_text(en)
        rejects(lambda: generate_seo_geo_assets(bad, site, True))
        bad = json.loads(json.dumps(config))
        bad['pages'][1]['file'] = 'missing.html'
        rejects(lambda: generate_seo_geo_assets(bad, site, True))
        bad = json.loads(json.dumps(config))
        bad['pages'][0]['path'] = '/?sku=pretend'
        rejects(lambda: generate_seo_geo_assets(bad, site, True))
        for domain in ('https://user:pass@target.example', 'https://target.example/other', 'https://target.example\nSitemap: evil'):
            rejects(lambda: generate_seo_geo_assets(dict(config, domain=domain), site, True))
        (site / 'index.html').write_text(en.replace('<head>', '<head><meta name="robots" content="noindex"><meta name="robots" content="index">'))
        rejects(lambda: generate_seo_geo_assets(config, site, True))
        rejects(lambda: generate_seo_geo_assets(dict(config, mode='draft', generate_llms=False), site, True))
        (site / 'llms.txt').unlink()
        generate_seo_geo_assets(dict(config, mode='draft', generate_llms=False), site, True)
        assert 'Disallow: /' in (site / 'robots.txt').read_text()
        assert not ET.parse(site / 'sitemap.xml').findall(f'{{{SM}}}url')
        assert schema_shape({'@context': 'https://schema.org', '@graph': [{'@type': 'Organization'}]})
        assert schema_shape([{'@type': 'WebPage'}])
        assert not schema_shape({'@context': 'https://schema.org', '@graph': []})
        assert audit_directory(site)
        nested = site / 'nested'
        nested.mkdir()
        (nested / 'bad.html').write_text('<html><h1>X</h1><img src="x"></html>')
        assert not audit_directory(site)
        completed = subprocess.run([sys.executable, str(Path(__file__).with_name('layout_typography_auditor.py')), str(site)], capture_output=True)
        assert completed.returncode == 1
        empty = root / 'empty'
        empty.mkdir()
        rejects(lambda: audit_directory(empty))
        (site / 'style.css').write_text(':root{--accent:#123456} h1{font-family:Arial}')
        extract_tokens(site / 'style.css', root / 'DESIGN.md')
        tokens = (root / 'DESIGN.md').read_text()
        assert '#123456' in tokens and 'Arial' in tokens and '1280px' not in tokens and '#e9e9d2' not in tokens
        (site / 'index.html').write_text(en.replace('<head>', '<head><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="fallback.html">'))
        (site / 'fallback.html').write_text(en)
        with ThreadingHTTPServer(('127.0.0.1', 0), partial(Fixture, directory=str(site))) as server:
            worker = threading.Thread(target=server.serve_forever, daemon=True)
            worker.start()
            try:
                evidence = root / 'evidence'
                assert not run_forensics(f'http://127.0.0.1:{server.server_port}/', evidence)
                manifest = json.loads((evidence / 'manifest.json').read_text())
                assert any('fallback.html' in gap['url'] for gap in manifest['failures'])
                assert all(len(item['sha256']) == 64 for item in manifest['resources'])
                assert (evidence / 'homepage.html').read_bytes() == (site / 'index.html').read_bytes()
                rejects(lambda: run_forensics(f'http://127.0.0.1:{server.server_port}/', evidence))
            finally:
                server.shutdown()
                worker.join()
        with ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietPreview, directory=str(site))) as server:
            worker = threading.Thread(target=server.serve_forever, daemon=True)
            worker.start()
            try:
                url = f'http://127.0.0.1:{server.server_port}'
                with urlopen(url) as response:
                    assert 'noindex' in response.headers['X-Robots-Tag']
                try:
                    urlopen(Request(url + '/api/rfq', data=b'{"email":"do-not-log@example.test"}'))
                except HTTPError as exc:
                    assert exc.code == 503
                else:
                    raise AssertionError('Disconnected RFQ reported success')
            finally:
                server.shutdown()
                worker.join()
    print('PASS: real routes/hreflang, identity isolation, draft/release, invalid input, nested audit, CSS evidence, HTTP types/hashes, disconnected RFQ.')


if __name__ == '__main__':
    main()
