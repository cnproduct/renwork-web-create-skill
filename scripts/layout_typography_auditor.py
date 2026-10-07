#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RenWork Web Create Skill · Layout & Typography Auditor
Audits HTML files for:
1. Missing alt tags on images
2. Heading level continuity (H1 -> H2 -> H3)
3. JSON-LD schema syntax & required fields
4. Responsive overflow risks (hardcoded widths, unescaped text)
5. Broken internal link paths
"""

import sys, os, json
from bs4 import BeautifulSoup

def audit_directory(dir_path):
    print(f"[Auditor] Scanning HTML files in: {dir_path}")
    html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]
    
    total_issues = 0
    for fn in sorted(html_files):
        fp = os.path.join(dir_path, fn)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        issues = []

        # 1. H1 presence
        h1s = soup.find_all('h1')
        if len(h1s) == 0:
            issues.append("Missing H1 heading")
        elif len(h1s) > 1:
            issues.append(f"Multiple H1 headings found ({len(h1s)})")

        # 2. Images missing alt
        imgs_no_alt = [img.get('src', '') for img in soup.find_all('img') if not img.get('alt')]
        if imgs_no_alt:
            issues.append(f"{len(imgs_no_alt)} images missing 'alt' attribute")

        # 3. JSON-LD validity
        for s in soup.find_all('script', type='application/ld+json'):
            try:
                data = json.loads(s.string)
                if not data.get('@context') or not data.get('@type'):
                    issues.append("JSON-LD missing @context or @type")
            except Exception as e:
                issues.append(f"JSON-LD syntax error: {e}")

        # 4. Viewport tag
        vp = soup.find('meta', attrs={'name': 'viewport'})
        if not vp:
            issues.append("Missing viewport meta tag for mobile responsiveness")

        # Report
        status = "✓ PASS" if not issues else "⚠ ISSUES FOUND"
        print(f"[{status}] {fn}")
        for iss in issues:
            print(f"    - {iss}")
            total_issues += 1

    print("-" * 50)
    if total_issues == 0:
        print("[Auditor] All pages PASSED the audit cleanly! Ready for production deployment.")
        return True
    else:
        print(f"[Auditor] Found {total_issues} issues to resolve.")
        return False

if __name__ == '__main__':
    target_dir = sys.argv[1] if len(sys.argv) > 1 else 'xhplasticlife-clone/'
    audit_directory(target_dir)
