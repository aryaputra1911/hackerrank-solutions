# ──────────────────────────────────────────────────
# Problem     Collections.OrderedDict()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-28, 12:13 a.m.
# ──────────────────────────────────────────────────

from collections import OrderedDict
import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    
    if not input_data:
        return
    n = int(input_data[0])

    ordered_dictionary = OrderedDict()
    for i in range(1, n + 1):
        line = input_data[i].split()
        price = int(line[-1])
        item_name = " ".join(line[:-1])
        if item_name in ordered_dictionary:
            ordered_dictionary[item_name] += price
        else:
            ordered_dictionary[item_name] = price

    for item, price in ordered_dictionary.items():
        print(f"{item} {price}")

solve()
