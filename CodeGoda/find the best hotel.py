import queue

MAX = 505
INF = int(1e9) + 7
graph = [[] for _ in range(MAX)]
dist = [INF for _ in range(MAX)]


class Node:
    def __init__(self, _id, _weight):
        self.id = _id
        self.weight = _weight

    def __lt__(self, other):
        return self.weight < other.weight


def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0

    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.weight

        for neighbor in graph[u]:
            if w + neighbor.weight < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.weight
                pq.put(Node(neighbor.id, dist[neighbor.id]))



def main():
    N, G = map(int,input().split())

    for _ in range(N):
        u, v, d = map(int, input().split())
        graph[u].append(Node(v, d))
        graph[v].append(Node(u, d))

    K = int(input())
    for _ in range(K):
        H, name, start, cost = map(str, input().split())
        Q, end = map(str,input().split())
        Dijkstra(int(start))
        if dist[int(end)] == INF:
            distance = 0
        else:
            distance = dist[int(end)]
    minimum = G * distance + cost
    print(minimum)



if __name__ == '__main__':
    main()