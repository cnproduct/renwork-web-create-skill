#!/usr/bin/env python3
"""Extract CSS candidates only; computed styles and browser measurements are required."""
import argparse
import re
from pathlib import Path


def extract_tokens(css_path, output_md_path):
    css = Path(css_path).read_text(encoding='utf-8')
    candidates = {
        'Custom properties': sorted(set(re.findall(r'--[\w-]+\s*:\s*[^;{}]+', css))),
        'Hex color candidates': sorted(set(re.findall(r'#[\da-fA-F]{8}\b|#[\da-fA-F]{6}\b|#[\da-fA-F]{4}\b|#[\da-fA-F]{3}\b', css))),
        'Font family candidates': sorted(set(re.findall(r'font-family\s*:\s*[^;{}]+', css))),
    }
    lines = ['# CSS design candidates', '', f'Source: {Path(css_path).name}', '',
             'Candidate extraction only. Verify computed styles, states, geometry and breakpoints in the browser; no design roles are inferred.', '']
    for name, values in candidates.items():
        lines += [f'## {name}', '', '```css', *values, '```', '']
    Path(output_md_path).write_text('\n'.join(lines), encoding='utf-8')
    print(f'CSS candidates saved to {output_md_path}; design system verification NOT_RUN.')
    return True


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('css_file')
    cli.add_argument('output_file')
    args = cli.parse_args()
    try:
        extract_tokens(args.css_file, args.output_file)
    except OSError as exc:
        cli.exit(1, f'Extraction failed: {exc}\n')
