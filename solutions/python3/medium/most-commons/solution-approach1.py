# ──────────────────────────────────────────────────
# Problem     Company Logo
# Difficulty  Medium
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-09, 09:35 a.m.
# ──────────────────────────────────────────────────

from collections import Counter

s = input()
count = Counter(s)
sorted_chars = sorted(count.items(), key=lambda x: (-x[1], x[0]))
for char, freq in sorted_chars[:3]:
    print(f"{char} {freq}")
