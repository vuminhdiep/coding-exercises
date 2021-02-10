# load input data

# number of node
import sys
sys.setrecursionlimit(10000000)

n = int(input())

visited = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
dist = [0] * (n + 1)

# it's tree, i.e. n -1 edges
for i in range(n - 1):
    inputs = input().split(' ')
    u = int(inputs[0])
    v = int(inputs[1])
    graph[u].append(v)
    graph[v].append(u)

# number of girls
q = int(input())
girls = []

for i in range(q):
    girl = int(input())
    girls.append(girl)


def dfs(node, distance):
    visited[node] = 1
    dist[node] = distance

    for child in graph[node]:
        if not visited[child]:
            dfs(child, distance + 1)


dfs(1, 0)

min_dis = 10000000
best_girl = 0
for girl in girls:
    if dist[girl] < min_dis:
        min_dis = dist[girl]
        best_girl = girl
    elif dist[girl] == min_dis and girl < best_girl:
        best_girl = girl

print(best_girl)