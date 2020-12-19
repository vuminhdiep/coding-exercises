# https://codeforces.com/problemset/problem/224/B

n, k = map(int, input().split())
a = [int(i) for i in input().split()]
d = {}
j = 1
for x in a:
    if len(d) == k:
        break
    d[x] = j
    j += 1

if len(d) == k:
    print(min(d.values()), max(d.values()))
else:
    print("-1 -1")