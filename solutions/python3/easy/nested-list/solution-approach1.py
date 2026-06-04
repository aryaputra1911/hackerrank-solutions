# ──────────────────────────────────────────────────
# Problem     Nested Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-04, 07:49 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    all_data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = list((name,score))
        all_data.append([name,score])
        
score = [i[1] for i in all_data]
unique = sorted(set(score))
result = unique[1]

name = [i[0] for i in all_data if i[1]==result]
name.sort()
for i in name:
    print(i)    
