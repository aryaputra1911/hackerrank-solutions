# ──────────────────────────────────────────────────
# Problem     Merge the Tools!
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-10, 11:02 p.m.
# ──────────────────────────────────────────────────

def merge_the_tools(string, k):
    # your code goes here
    chunks = [string[i:i + k]for i in range(0, len(string), k)]
    for i in chunks:
        unique_letters = list(dict.fromkeys(i))
        results = "".join(unique_letters)
        print(results)
    return
