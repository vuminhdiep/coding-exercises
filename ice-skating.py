n = int(input())
rank = [-1] * 9999


def drift(x):
    if rank[x] < 0:
        rank[x] = x
    if x != rank[x]:
        rank[x] = drift(rank[x])
    return rank[x]


for i in range(n):
    a, b = map(int, input().split())
    b += 1000
    n -= (rank[a] >= 0) + (rank[b] >= 0) - (drift(a) == drift(b))
    rank[drift(a)] = drift(b)
print(n - 1)
