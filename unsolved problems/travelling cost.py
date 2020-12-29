# Đề cho biết các địa điểm được đánh số từ 00 đến 500500 và danh sách các đường đi, vậy ta có thể thấy đây là một đồ thị có 501501 đỉnh và các con đường sẽ là các cạnh của đồ thị.

# Từ danh sách cạnh, tạo đồ thị, sau đó chạy Dijkstra từ đỉnh UU. Sau khi chạy xong dựa vào mảng chi phí distdist để tìm chi phí đến các đỉnh cần tìm. Nếu đỉnh nào chi phí là vô cực (INF) thì sẽ không có đường đi đến đó.

# Độ phức tạp: \mathcal {O} \left( E*log(V) \right)O(E∗log(V)) với EE là số lượng cạnh (cung), VV là số lượng đỉnh trong đồ thị.

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
 
N = int(input())
for _ in range(N):
    A, B, W = map(int, input().split())
    graph[A].append(Node(B, W))
    graph[B].append(Node(A, W))
 
S = int(input())
Dijkstra(S)
 
Q = int(input())
for _ in range(Q):
    V = int(input())
    print(dist[V] if dist[V] != INF else "NO PATH")