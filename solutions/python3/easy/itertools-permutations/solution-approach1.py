# ──────────────────────────────────────────────────
# Problem     itertools.permutations()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-24, 08:24 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

InputUsers = input().split()
a = list(permutations(InputUsers[0], int(InputUsers[1])))
for i in sorted(a):
    b = ",".join(i)
    clean = b.replace(",", "")
    print(clean)
