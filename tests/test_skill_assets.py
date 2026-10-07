#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for renwork-web-create-skill assets and scripts integrity.
"""

import os, sys, json

def test_references():
    ref_dir = os.path.join(os.path.dirname(__file__), '..', 'references')
    mandatory_files = [
        'benchmark-discovery-methodology.md',
        'site-protection.md',
        'procurement-components.md',
        'b2b-design-tokens.md',
        'geo-citability-guide.md',
        'b2b-seo-schema-spec.md',
        'pixel-clone-contract.md',
        'turnstile.md',
        'rfq-backend.md'
    ]
    for mf in mandatory_files:
        p = os.path.join(ref_dir, mf)
        assert os.path.exists(p), f"Missing mandatory reference: {mf}"
        assert os.path.getsize(p) > 200, f"File {mf} is too small"
    print("✓ All 9 mandatory references verified.")

def test_scripts():
    scripts_dir = os.path.join(os.path.dirname(__file__), '..', 'scripts')
    mandatory_scripts = [
        'site_forensics.py',
        'extract_design_tokens.py',
        'geo_seo_engine.py',
        'layout_typography_auditor.py',
        'dev_server.py'
    ]
    for ms in mandatory_scripts:
        p = os.path.join(scripts_dir, ms)
        assert os.path.exists(p), f"Missing mandatory script: {ms}"
    print("✓ All 5 core scripts verified.")

def test_industries_json():
    ind_file = os.path.join(os.path.dirname(__file__), '..', 'assets', 'industries.json')
    assert os.path.exists(ind_file), "Missing assets/industries.json"
    with open(ind_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert 'industries' in data, "industries array missing in industries.json"
    print(f"✓ industries.json verified with {len(data['industries'])} industry profiles.")

if __name__ == '__main__':
    test_references()
    test_scripts()
    test_industries_json()
    print("All renwork-web-create-skill tests PASSED!")
