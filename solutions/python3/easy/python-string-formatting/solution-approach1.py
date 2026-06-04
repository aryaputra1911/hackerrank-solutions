# ──────────────────────────────────────────────────
# Problem     String Formatting
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-04, 09:11 p.m.
# ──────────────────────────────────────────────────

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        d= str(i).rjust(width)
        o= oct(i)[2:].rjust(width)
        h= hex(i).upper()[2:].rjust(width)
        b= bin(i)[2:].rjust(width)
        
        print(f"{d} {o} {h} {b}")
    return
    

