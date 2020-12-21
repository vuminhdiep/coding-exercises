def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u


def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up != vp:
        parent[up] = vp
        cnt[vp] += cnt[up]


if __name__ == '__main__':
    t = int(input())
    for test in range(t):
        n, m = map(int, input().split())
        parent = [[] for l in range(n+1)]
        for i in range(1, n+1):
            parent[i] = i

        cnt = [1 for i in range(n+1)]
        for j in range(m):
            u, v = map(int, input().split())
            unionSet(u, v)

        ans = 0
        for k in range(1, n+1):
            ans = max(ans, cnt[i])
        print(ans)
