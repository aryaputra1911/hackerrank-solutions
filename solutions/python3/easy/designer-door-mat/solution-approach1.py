# ──────────────────────────────────────────────────
# Problem     Designer Door Mat
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-12, 08:40 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
def door_mat(n, m):
    for i in range(1, n, 2):
        print((i*".|.").center(m, "-"))
    print("WELCOME".center(m, "-"))
    for i in range(n-2, -1, -2):
        print((i*".|.").center(m, "-"))

n, m = map(int, input().split())
door_mat(n, m)
