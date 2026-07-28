# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
# Problem     Set .add() 
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-28, 11:04 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
n = set()

for i in range(int(a)):
    n.add(input())
print(len(list(n)))

