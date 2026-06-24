# ──────────────────────────────────────────────────
# Problem     itertools.product()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-24, 07:22 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

A=map(int,input().split())
B=map(int,input().split())

a = list(A)
b = list(B)
test = [a, b]
Final = list(product(*test))
for i in Final:
    print(i, end=" ")


