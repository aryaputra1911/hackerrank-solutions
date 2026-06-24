# ──────────────────────────────────────────────────
# Problem     Introduction to Sets
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-24, 03:05 p.m.
# ──────────────────────────────────────────────────

def average(array):
    # your code goes here
    unique = list(set(array))
    return sum(unique)/len(unique)
