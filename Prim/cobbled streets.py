import queue

INF = 1e9


class Node:
    def __init__(self, index, dist):
        self.index = index
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


def Prim(start):
    pq = queue.PriorityQueue()
    pq.put(Node(start, 0))
    dist[start] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.index
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.index
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u
    res = 0
    for i in range(n):
        if visited[i] == True:
            res += dist[i]
    return res
if __name__ == '__main__':

    t = int(input())
    for _ in range(t):
        p = int(input())
        n = int(input())
        m = int(input())
        graph = [[] for i in range(n)]
        dist = [INF for i in range(n)]
        path = [-1 for i in range(n)]
        visited = [False for i in range(n)]
        for i in range(m):
            u, v, w = map(int, input().split())
            u -= 1
            v -= 1
            graph[u].append(Node(v, w))
            graph[v].append(Node(u, w))

        res = Prim(0)
        print(res*p)