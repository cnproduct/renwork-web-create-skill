#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RenWork Web Create Skill · Site Forensics Engine
Deeply inspects target prototype website, extracts DOM, CSS, JSON-LD Schemas, Sitemaps, and SKU Catalogs.
Based on 'Evidence-Driven Forensics' and 'Zero-Hallucination Clone Methodology'.
"""

import sys, os, urllib.request, ssl, re, json
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

def run_forensics(target_url, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    print(f"[Forensics] Starting probe against: {target_url}")
    
    # 1. Fetch Homepage
    req = urllib.request.Request(target_url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            raw_html = resp.read().decode('utf-8', errors='ignore')
            resp_headers = dict(resp.getheaders())
    except Exception as e:
        print(f"[Error] Failed to fetch target: {e}")
        return False

    with open(os.path.join(output_dir, 'headers.json'), 'w', encoding='utf-8') as f:
        json.dump(resp_headers, f, indent=2)
    with open(os.path.join(output_dir, 'homepage.html'), 'w', encoding='utf-8') as f:
        f.write(raw_html)

    soup = BeautifulSoup(raw_html, 'html.parser')
    
    # 2. Extract SEO Metadata
    seo_meta = {
        'title': soup.title.string.strip() if soup.title else '',
        'meta_description': '',
        'meta_keywords': '',
        'canonical': '',
        'og_tags': {},
        'twitter_tags': {}
    }
    for m in soup.find_all('meta'):
        name = m.get('name', '').lower()
        prop = m.get('property', '').lower()
        content = m.get('content', '')
        if name == 'description':
            seo_meta['meta_description'] = content
        elif name == 'keywords':
            seo_meta['meta_keywords'] = content
        elif prop.startswith('og:'):
            seo_meta['og_tags'][prop] = content
        elif name.startswith('twitter:'):
            seo_meta['twitter_tags'][name] = content

    can = soup.find('link', rel='canonical')
    if can:
        seo_meta['canonical'] = can.get('href', '')

    with open(os.path.join(output_dir, 'seo_metadata.json'), 'w', encoding='utf-8') as f:
        json.dump(seo_meta, f, indent=2, ensure_ascii=False)

    # 3. Extract JSON-LD Schemas
    schemas = []
    for s in soup.find_all('script', type='application/ld+json'):
        if s.string:
            try:
                schemas.append(json.loads(s.string))
            except Exception:
                pass
    with open(os.path.join(output_dir, 'schemas.json'), 'w', encoding='utf-8') as f:
        json.dump(schemas, f, indent=2, ensure_ascii=False)

    # 4. Fetch CSS Files
    css_urls = []
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href')
        if href:
            css_urls.append(urljoin(target_url, href))

    css_dir = os.path.join(output_dir, 'css')
    os.makedirs(css_dir, exist_ok=True)
    for idx, u in enumerate(css_urls):
        try:
            req_css = urllib.request.Request(u, headers=headers)
            with urllib.request.urlopen(req_css, context=ctx, timeout=15) as r:
                css_content = r.read().decode('utf-8', errors='ignore')
                with open(os.path.join(css_dir, f'bundle_{idx}.css'), 'w', encoding='utf-8') as f:
                    f.write(css_content)
        except Exception as e:
            print(f"[Warning] Failed to fetch CSS {u}: {e}")

    # 5. Probe robots.txt and sitemap.xml
    for res_name in ['robots.txt', 'sitemap.xml']:
        try:
            u = urljoin(target_url, '/' + res_name)
            req_r = urllib.request.Request(u, headers=headers)
            with urllib.request.urlopen(req_r, context=ctx, timeout=10) as r:
                with open(os.path.join(output_dir, res_name), 'w', encoding='utf-8') as f:
                    f.write(r.read().decode('utf-8', errors='ignore'))
        except Exception:
            pass

    print(f"[Forensics] Evidence successfully saved to: {output_dir}")
    print(f" - Title: {seo_meta['title']}")
    print(f" - JSON-LD Schemas captured: {len(schemas)}")
    print(f" - CSS bundles captured: {len(css_urls)}")
    return True

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'https://www.xhplasticlife.com/'
    out = sys.argv[2] if len(sys.argv) > 2 else './evidence'
    run_forensics(target, out)
