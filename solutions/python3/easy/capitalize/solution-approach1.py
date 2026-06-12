# ──────────────────────────────────────────────────
# Problem     Capitalize!
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-12, 09:33 p.m.
# ──────────────────────────────────────────────────



# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    capital = [i.capitalize() for i in words]
    return " ".join(capital)
