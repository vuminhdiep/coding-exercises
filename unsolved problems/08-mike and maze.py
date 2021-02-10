# Có hai cách để giải quyết bài này.

# Cách 1: Do số lượng đỉnh NN bé (100100 đỉnh) nên bạn có thể chạy Dijkstra ở mỗi đỉnh rồi tìm đường đi từ các đỉnh đến đỉnh thoát ra. Nếu chi phí \le T≤T thì bạn sẽ tăng số lượng con chuột lên.

# Cách 2: Cách này bạn chỉ chạy Dijsktra 11 lần, bạn sẽ chạy Dijkstra từ đỉnh thoát ra. Tuy nhiên trước khi chạy Dijkstra từ đỉnh này bạn phải quay ngược hướng toàn bộ đồ thị lại. Vì bạn cần tìm đường đi từ các đỉnh khác tới lối thoát, giờ bạn tìm đường đi từ đỉnh lối thoát đến các đỉnh khác, thì bạn cần phải quay ngược hướng các đồ thị lại để tìm đường đi. Sau đó xét các chi phí, chi phí nào \le T≤T thì tăng số lượng chuột có thể thoát lên.

import queue
MAX = 105
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
 
N = int(input())
E = int(input())
T = int(input())
M = int(input())
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[v].append(Node(u, w))
 
Dijkstra(E)
 
count = 0
for i in range(1, N + 1):
    if dist[i] <= T:
        count += 1
 
print(count)