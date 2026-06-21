# ──────────────────────────────────────────────────
# Problem     collections.Counter()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-21, 09:46 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
import sys

all_shoes = int(input())
all_sizes = Counter(map(int, input().split()))
num_customers = int(input())

total_money = 0

for i in range(num_customers):
    size, price = map(int, input().split())
    
    if all_sizes[size] > 0:
        total_money += price
        all_sizes[size] -= 1
print(total_money)
    
