# ──────────────────────────────────────────────────
# Problem     Text Wrap
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-10, 05:10 p.m.
# ──────────────────────────────────────────────────



def wrap(string, max_width):
    wrap = textwrap.wrap(string, width = max_width)
    return "\n".join(wrap)

