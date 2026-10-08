#!/usr/bin/env python3
"""Static HTML checks only: headings, alt presence, viewport and JSON-LD shape."""
import argparse
import json
import sys
from pathlib import Path
from site_forensics import PageParser


def schema_shape(data):
    if isinstance(data, list):
        return bool(data) and all(schema_shape(item) for item in data)
    if not isinstance(data, dict):
        return False
    if '@graph' in data:
        graph = data['@graph']
        return bool(data.get('@context')) and isinstance(graph, list) and bool(graph) and all(
            isinstance(item, dict) and bool(item.get('@type')) for item in graph)
    return bool(data.get('@type'))


def audit_directory(dir_path):
    root = Path(dir_path)
    if not root.is_dir():
        raise ValueError('Build directory does not exist')
    pages = sorted(root.rglob('*.html'))
    if not pages:
        raise ValueError('No HTML files found; cannot pass an empty audit')
    count = 0
    for file in pages:
        parser = PageParser()
        parser.feed(file.read_text(encoding='utf-8'))
        issues = []
        if parser.h1_count != 1:
            issues.append(f'Expected one primary H1; found {parser.h1_count}')
        if 'viewport' not in parser.meta:
            issues.append('Missing viewport')
        if not parser.lang:
            issues.append('Missing HTML language')
        if any('alt' not in image for image in parser.images):
            issues.append('Image missing alt attribute (empty alt is allowed for decoration)')
        for raw in parser.schemas:
            try:
                if not schema_shape(json.loads(raw)):
                    issues.append('Unexpected JSON-LD type/graph shape')
            except ValueError:
                issues.append('Invalid JSON-LD JSON')
        count += len(issues)
        print(f"{'FAIL' if issues else 'PASS'} {file.relative_to(root)}: {', '.join(issues) or 'static checks'}")
    print(f'{len(pages)} pages, {count} static issues. Visual overflow, browser interactions and live SEO/GEO NOT_RUN.')
    return count == 0


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('directory')
    args = cli.parse_args()
    try:
        sys.exit(0 if audit_directory(args.directory) else 1)
    except (OSError, ValueError) as exc:
        cli.exit(1, f'Audit failed: {exc}\n')
