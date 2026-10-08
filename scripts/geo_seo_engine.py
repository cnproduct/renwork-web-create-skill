#!/usr/bin/env python3
"""Validate rendered routes and prepare SEO assets; does not inject page markup."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET
from site_forensics import PageParser

SM = 'http://www.sitemaps.org/schemas/sitemap/0.9'
XHTML = 'http://www.w3.org/1999/xhtml'


def generate_seo_geo_assets(config_dict, output_dir, overwrite=False):
    root = Path(output_dir).resolve(strict=True)
    domain = config_dict['domain'].rstrip('/')
    origin = urlsplit(domain)
    if (any(c.isspace() or ord(c) < 32 for c in domain) or origin.scheme != 'https' or not origin.netloc or origin.path or origin.query
            or origin.fragment or origin.username or origin.password):
        raise ValueError('domain must be an HTTPS origin without credentials or path')
    for key in ('brand_name', 'company_name'):
        if not isinstance(config_dict.get(key), str) or not config_dict[key].strip():
            raise ValueError(f'{key} is required')
    mode = config_dict.get('mode', 'draft')
    if mode not in ('draft', 'release'):
        raise ValueError('mode must be draft or release')
    pages = config_dict['pages']
    if not isinstance(pages, list) or not pages:
        raise ValueError('pages must be a nonempty list of actual HTML routes')
    by_path = {}
    files = set()
    for p in pages:
        route = p['path']
        parsed = urlsplit(route)
        if (not route.startswith('/') or route.startswith('//') or parsed.scheme or parsed.netloc
                or parsed.query or parsed.fragment or any(c.isspace() for c in route)
                or '\\' in route or any(part in ('.', '..') for part in route.split('/'))):
            raise ValueError(f'Invalid canonical route: {route}')
        if route in by_path:
            raise ValueError(f'Duplicate route: {route}')
        file = (root / p['file']).resolve(strict=True)
        if Path(p['file']).is_absolute() or root not in file.parents or file.suffix.lower() != '.html':
            raise ValueError('file must be an HTML file inside the build directory')
        if file in files:
            raise ValueError('Each canonical route must have its own HTML file')
        files.add(file)
        if not p.get('title') or not re.fullmatch(r'[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*', p.get('lang', '')):
            raise ValueError('Every page needs a title and a valid language tag')
        parser = PageParser()
        parser.feed(file.read_text(encoding='utf-8'))
        if parser.lang.lower() != p['lang'].lower():
            raise ValueError(f'HTML language mismatch: {route}')
        if mode == 'release':
            if any('noindex' in v.lower() or 'none' in re.split(r'[\s,]+', v.lower())
                   for k, v in parser.meta.items() if k in ('robots', 'googlebot', 'bingbot')):
                raise ValueError(f'noindex HTML cannot enter a release sitemap: {route}')
            canonical = [a.get('href') for a in parser.links if 'canonical' in a.get('rel', '').split()]
            if canonical and canonical != [domain + route]:
                raise ValueError(f'Existing canonical mismatch: {route}')
        by_path[route] = p
    for p in pages:
        alternatives = p.get('alternates', {})
        if alternatives and alternatives.get(p['lang']) != p['path']:
            raise ValueError('hreflang must include the page itself')
        for lang, route in alternatives.items():
            other = by_path.get(route)
            if (other is None or (lang != 'x-default' and other['lang'] != lang)
                    or other.get('alternates', {}) != alternatives):
                raise ValueError('hreflang must target existing, language-matched, reciprocal pages')
    ET.register_namespace('', SM)
    ET.register_namespace('xhtml', XHTML)
    sitemap = ET.Element(f'{{{SM}}}urlset')
    records = []
    for p in pages:
        canonical = domain + p['path']
        if mode == 'release':
            node = ET.SubElement(sitemap, f'{{{SM}}}url')
            ET.SubElement(node, f'{{{SM}}}loc').text = canonical
            for lang, route in p.get('alternates', {}).items():
                ET.SubElement(node, f'{{{XHTML}}}link', rel='alternate', hreflang=lang, href=domain + route)
        graph = [
            {'@type': 'Organization', '@id': domain + '/#organization', 'name': config_dict['company_name'], 'url': domain + '/'},
            {'@type': 'WebSite', '@id': domain + '/#website', 'name': config_dict['brand_name'], 'url': domain + '/', 'publisher': {'@id': domain + '/#organization'}},
            {'@type': 'WebPage', '@id': canonical + '#webpage', 'url': canonical, 'name': p['title'], 'inLanguage': p['lang'], 'isPartOf': {'@id': domain + '/#website'}},
        ]
        records.append({'file': p['file'], 'canonical': canonical, 'title': p['title'],
                        'description': p.get('description', ''), 'robots': 'noindex, nofollow' if mode == 'draft' else 'index, follow',
                        'hreflang': {k: domain + v for k, v in p.get('alternates', {}).items()},
                        'schema': {'@context': 'https://schema.org', '@graph': graph}})
    robots = 'User-agent: *\nDisallow: /\n' if mode == 'draft' else f'User-agent: *\nAllow: /\nSitemap: {domain}/sitemap.xml\n'
    outputs = {'robots.txt': robots, 'sitemap.xml': ET.tostring(sitemap, encoding='unicode', xml_declaration=True),
               'seo-pages.json': json.dumps({'status': 'PREPARED_NOT_APPLIED', 'mode': mode, 'pages': records}, ensure_ascii=False, indent=2)}
    if config_dict.get('generate_llms', False):
        if mode != 'release':
            raise ValueError('llms index is only for release public pages')
        outputs['llms.txt'] = f"# {config_dict['brand_name']}\n\n> Public page index for {config_dict['company_name']}.\n\n## Pages\n" + '\n'.join(
            f"- [{p['title']}]({domain + p['path']}): {p.get('description', '')}" for p in pages) + '\n'
    if not config_dict.get('generate_llms', False) and (root / 'llms.txt').exists():
        raise ValueError('Old llms.txt would remain stale; review and remove it before disabling the index')
    for name in outputs:
        dest = root / name
        if dest.is_symlink() or (dest.exists() and not overwrite):
            raise ValueError(f'Output exists or is a symlink: {name}; review before --overwrite')
    for name, content in outputs.items():
        (root / name).write_text(content, encoding='utf-8')
    print(f'Prepared {len(records)} page records in {root}; apply to source templates, rebuild and verify. Indexing/citations NOT_RUN.')
    return records


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('output_dir')
    cli.add_argument('--config', required=True, type=Path)
    cli.add_argument('--overwrite', action='store_true')
    args = cli.parse_args()
    try:
        generate_seo_geo_assets(json.loads(args.config.read_text(encoding='utf-8')), args.output_dir, args.overwrite)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        cli.exit(1, f'Generation failed: {exc}\n')
