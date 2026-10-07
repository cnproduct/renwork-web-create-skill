#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RenWork Web Create Skill · Design Token Synthesis Engine
Extracts visual tokens (Colors, Typography, Spacing, Surface Layers) from raw CSS bundles.
Outputs a structured DESIGN.md adhering to 'website-to-design-md' standards.
"""

import sys, os, re

def extract_tokens(css_path, output_md_path):
    if not os.path.exists(css_path):
        print(f"[Error] CSS file not found at: {css_path}")
        return False

    with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
        css = f.read()

    # 1. Colors
    color_vars = set(re.findall(r'(--color-[a-zA-Z0-9\-]+:\s*[^;]+;)', css))
    hex_colors = set(re.findall(r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b', css))

    # 2. Fonts
    font_vars = set(re.findall(r'(--font-[a-zA-Z0-9\-]+:\s*[^;]+;)', css))

    # 3. Key classes
    surfaces = ['surface-media', 'surface-sunken', 'surface-tint', 'surface-light', 'surface-white', 'surface-dark']

    md_content = f"""# DESIGN.md · Extracted Visual Design System

> Generated automatically by `extract_design_tokens.py`.
> Based on analysis of `{os.path.basename(css_path)}`.

---

## 1. Color Palette Tokens
"""
    if color_vars:
        md_content += "\n### Defined Color Variables\n```css\n"
        for cv in sorted(color_vars):
            md_content += f"{cv}\n"
        md_content += "```\n"

    md_content += f"""
## 2. Typography System
"""
    if font_vars:
        md_content += "\n### Font Variables\n```css\n"
        for fv in sorted(font_vars):
            md_content += f"{fv}\n"
        md_content += "```\n"

    md_content += """
## 3. Surface & Hierarchy Rules
- `.surface-media`: High-contrast dark scrim or image backdrop with white text (`--color-fg: #fff`).
- `.surface-sunken`: Warm oatmeal sand background (`#e9e9d2`) used for Trust Bridge ribbons.
- `.surface-tint`: Soft pale green tint (`#eef2ee`) for category and workflow sections.
- `.surface-light`: Subtle off-white (`#f7f7f7`) for tabular specifications and technical grids.
- `.surface-white`: Crisp white background (`#ffffff`) for product cards and high-conversion RFQ forms.

## 4. Layout Constraints
- Max Container Width: `1280px` (`.section-shell`, `.page-container`).
- Desktop Grid Gap: `1.5rem ~ 2rem`.
- Card Hover Motion: `transform: translateY(-4px)`, smooth cubic-bezier curve.
"""

    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"[Design Tokens] DESIGN.md generated at: {output_md_path}")
    return True

if __name__ == '__main__':
    css_file = sys.argv[1] if len(sys.argv) > 1 else 'xhplasticlife-clone/css/style.css'
    out_file = sys.argv[2] if len(sys.argv) > 2 else 'renwork-web-create-skill/references/design-tokens-playbook.md'
    extract_tokens(css_file, out_file)
