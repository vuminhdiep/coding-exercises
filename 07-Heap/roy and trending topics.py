import heapq
n = int(input())
ls = []
for _ in range(n):
    id, z, p, l, c, s = map(int, input().split())
    z_score = p * 50 + l * 5 + c * 10 + s * 20
    change = z_score - z
    ls.append([change, id, z_score])

data = heapq.nlargest(5, ls)

for i, j, k in data:
    print(j, k)