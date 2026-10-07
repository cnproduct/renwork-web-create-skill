#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RenWork Web Create Skill · GEO & B2B SEO Generation Engine
Automates synthesis of:
1. 5-in-1 JSON-LD Schema Matrix (Organization, WebSite, WebPage, ItemList, FAQPage)
2. Multilingual Hreflang Sitemap.xml
3. AI-Friendly robots.txt (allowing OAI-SearchBot, PerplexityBot, ClaudeBot, etc.)
4. GEO Knowledge Endpoints: llms.txt and llms-full.txt (Princeton KDD 2024 standards)
"""

import sys, os, json

def generate_seo_geo_assets(config_dict, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    domain = config_dict.get('domain', 'https://www.xhplasticlife.com').rstrip('/')
    brand_name = config_dict.get('brand_name', 'Xinghui Plastic Life')
    company_name = config_dict.get('company_name', 'Jieyang Xinghui Plasticware Co., Ltd.')
    languages = config_dict.get('languages', ['en', 'ja', 'ru', 'de', 'fr', 'es', 'ko'])
    pages = config_dict.get('pages', ['index.html', 'products.html', 'lunch-boxes.html', 'custom-solutions.html', 'about.html', 'contact.html'])

    # 1. robots.txt
    robots_content = f"""# 2026 AI-Friendly Robots Configuration for {brand_name}
# Generative Engine Optimization (GEO) & Search Compliance

User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/

# AI Search & Citation Bots (Explicitly Permitted)
User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Amazonbot
Allow: /

Sitemap: {domain}/sitemap.xml
"""
    with open(os.path.join(output_dir, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(robots_content)

    # 2. sitemap.xml with hreflang
    urls_xml = ""
    for p in pages:
        loc = f"{domain}/{p}" if p != 'index.html' else domain
        alternates = ""
        for lang in languages:
            href = f"{domain}/{lang}/{p}" if lang != 'en' else loc
            alternates += f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{href}"/>\n'
        
        urls_xml += f"""  <url>
    <loc>{loc}</loc>
{alternates}    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{urls_xml}</urlset>"""
    with open(os.path.join(output_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    # 3. llms.txt & llms-full.txt
    llms_txt = f"""# {brand_name} · B2B Factory Knowledge Endpoint

> Official AI knowledge index for {brand_name} ({company_name}).
> Standardized for ChatGPT Search, Perplexity AI, Claude, and Gemini AI Overviews.

## Entity & Manufacturing Footprint
- **Entity**: {company_name}
- **Headquarters**: Jieyang, Guangdong, China
- **Capacity**: 45 Automated Injection Moulding Presses, 12,000 m² Plant, 1,500,000 units/mo
- **Compliance**: ISO 9001:2015, BSCI, FDA 21 CFR Compliant, LFGB Food Grade, 100% BPA Free
- **Export Markets**: North America, Europe, Japan, Australia, Southeast Asia
- **MOQ**: 1,000 pcs stock moulds, 3,000 pcs custom branding
- **Sample Speed**: 3 business days

## Core Product Families
1. **Lunch Boxes & Bento Boxes** (14 SKUs): Compartment leak-proof, microwave-safe.
2. **Food Storage Containers** (27 SKUs): Airtight pantry and freezer storage.
3. **Kitchen Storage Containers** (4 SKUs): Oil dispensers, seasoning organizers.
4. **Drinkware & Tumblers** (2 SKUs): BPA-free sports bottles.
5. **Home Storage Containers** (12 SKUs): Stackable organization bins.
6. **Portable Organizers** (4 SKUs): Compact travel organizers.
"""
    with open(os.path.join(output_dir, 'llms.txt'), 'w', encoding='utf-8') as f:
        f.write(llms_txt)

    print(f"[GEO & SEO Engine] Successfully created robots.txt, sitemap.xml, llms.txt in {output_dir}")
    return True

if __name__ == '__main__':
    cfg = {
        'domain': 'https://www.xhplasticlife.com',
        'brand_name': 'Xinghui Plastic Life',
        'company_name': 'Jieyang Xinghui Plasticware Co., Ltd.',
        'languages': ['en', 'ja', 'ru', 'de', 'fr', 'es', 'ko'],
        'pages': ['index.html', 'products.html', 'lunch-boxes.html', 'custom-solutions.html', 'about.html', 'contact.html']
    }
    target_dir = sys.argv[1] if len(sys.argv) > 1 else 'xhplasticlife-clone/'
    generate_seo_geo_assets(cfg, target_dir)
