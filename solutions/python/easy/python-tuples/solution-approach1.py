# ──────────────────────────────────────────────────
# Problem     Tuples 
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python
# Status      Accepted
# Submitted   2026-06-08, 09:23 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    tpl = tuple(integer_list)
    print(hash(tpl))
