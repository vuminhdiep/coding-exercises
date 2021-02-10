dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
MAX = 51
visited = [[False] * MAX for _ in range(MAX)]
table = []
lakes = []


def DFS(sr, sc):
    s = [(sr, sc)]
    visited[sr][sc] = True

    isOcean = False
    temp = []

    while len(s):
        ur, uc = s.pop()
        temp.append((ur, uc))

        if ur == 0 or uc == 0 or ur == n - 1 or uc == m - 1:
            isOcean = True

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if r in range(n) and c in range(m) and table[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                s.append((r, c))

    if not isOcean:
        lakes.append(temp)


n, m, k = map(int, input().split())

for _ in range(n):
    table.append(list(input()))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and table[i][j] == '.':
            DFS(i, j)

lakes.sort(key=lambda lake: len(lake))
sum_cell = 0

for i in range(len(lakes) - k):
    sum_cell += len(lakes[i])
    for r, c in lakes[i]:
        table[r][c] = '*'

print(sum_cell)

for i in range(n):
    print(''.join(table[i]))