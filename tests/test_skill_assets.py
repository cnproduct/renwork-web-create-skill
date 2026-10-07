#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for renwork-web-create-skill v4 assets and scripts integrity.
"""

import os, sys, json

def test_references():
    ref_dir = os.path.join(os.path.dirname(__file__), '..', 'references')
    mandatory_files = [
        'buyer-and-trade-research.md',
        'mechanism-distillation-and-creative-direction.md',
        'benchmark-discovery-methodology.md',
        'site-protection.md',
        'procurement-components.md',
        'b2b-design-tokens.md',
        'geo-citability-guide.md',
        'b2b-seo-schema-spec.md',
        'pixel-clone-contract.md',
        'traffic-and-originality.md',
        'skill-fusion.md',
        'turnstile.md',
        'rfq-backend.md'
    ]
    for mf in mandatory_files:
        p = os.path.join(ref_dir, mf)
        assert os.path.exists(p), f"Missing mandatory reference: {mf}"
        assert os.path.getsize(p) > 200, f"File {mf} is too small"
    print(f"✓ All {len(mandatory_files)} mandatory references verified.")

def test_templates():
    tmpl_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
    mandatory_templates = [
        'BUYER_STRATEGY.md',
        'edge-worker.mjs'
    ]
    for mt in mandatory_templates:
        p = os.path.join(tmpl_dir, mt)
        assert os.path.exists(p), f"Missing mandatory template: {mt}"
        assert os.path.getsize(p) > 100, f"Template {mt} is too small"
    print(f"✓ All {len(mandatory_templates)} mandatory templates verified.")

def test_scripts():
    scripts_dir = os.path.join(os.path.dirname(__file__), '..', 'scripts')
    mandatory_scripts = [
        'site_forensics.py',
        'extract_design_tokens.py',
        'geo_seo_engine.py',
        'layout_typography_auditor.py',
        'test_tools.py',
        'dev_server.py'
    ]
    for ms in mandatory_scripts:
        p = os.path.join(scripts_dir, ms)
        assert os.path.exists(p), f"Missing mandatory script: {ms}"
    print(f"✓ All {len(mandatory_scripts)} core scripts verified.")

def test_industries_json():
    ind_file = os.path.join(os.path.dirname(__file__), '..', 'assets', 'industries.json')
    assert os.path.exists(ind_file), "Missing assets/industries.json"
    with open(ind_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert 'industries' in data, "industries array missing in industries.json"
    print(f"✓ industries.json verified with {len(data['industries'])} industry profiles.")

if __name__ == '__main__':
    test_references()
    test_templates()
    test_scripts()
    test_industries_json()
    print("All renwork-web-create-skill v4 tests PASSED cleanly!")
