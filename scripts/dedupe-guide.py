#!/usr/bin/env python3
"""Drops repeated programmes (same channel and start time) from guide.xml, in place.

The Pickx grab repeats about a third of all programmes (those around midnight appear in two
days' responses). The iptv-org output has exactly one <programme> per line, so this works
line by line and leaves everything else untouched.

Usage: python3 scripts/dedupe-guide.py public/guide.xml
"""
import re
import sys

path = sys.argv[1]
programme = re.compile(r'^<programme start="([^"]+)"[^>]*channel="([^"]+)"')

seen = set()
kept_lines = []
dropped = 0
with open(path, encoding='utf-8') as guide:
    for line in guide:
        match = programme.match(line)
        if match:
            key = (match.group(2), match.group(1))
            if key in seen:
                dropped += 1
                continue
            seen.add(key)
        kept_lines.append(line)

with open(path, 'w', encoding='utf-8') as guide:
    guide.writelines(kept_lines)
print(f"dropped {dropped} duplicate programmes, kept {len(seen)}")
