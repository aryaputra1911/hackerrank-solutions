# ──────────────────────────────────────────────────
# Problem     Polar Coordinates
# Difficulty  Easy
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-24, 09:49 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
InputUsers = input()
complexnum = complex(InputUsers)
magnitudo, fase = cmath.polar(complexnum)
print(magnitudo)
print(fase)
