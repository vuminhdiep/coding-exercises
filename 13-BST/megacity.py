n, s = map(int, input().split())
d = {}

for i in range(n):
    x, y, k = map(int, input().split())
    dist = (x ** 2 + y ** 2) ** (1 / 2)
    if dist not in d:
        d[dist] = k
    else:
        d[dist] += k

lstKey = sorted(d)
ans = None
for ele in lstKey:
    s += d[ele]
    if s >= 1000000:
        ans = ele
        break
if ans == None:
    print(-1)
else:
    print("%.7f" % (ele))