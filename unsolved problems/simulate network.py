# Đầu tiên bạn sẽ tìm cây khung nhỏ nhất của đồ thị đề bài cho, sau đó lần lượt thay các cạnh có độ trễ lớn bằng cách cạnh có độ trễ nhỏ hơn trong QQ sợi cáp được cho.
#
# Sau khi tìm được cây khung nhỏ nhất tạo thành từ các sợi cáp sẵn có, bạn sẽ thay các sợi cáp lớn nhất bằng những sợi cáp mới có độ trễ nhỏ nhất có thể để giảm chi phí xuống. Có thể sử dụng 2 heap (1 heap max cho các sợi cáp trong cây khung để ưu tiên thay những sợi lớn nhất và 1 heap min cho các sợi cáp mới để ưu tiên chọn những sợi cáp nhỏ nhất). Hoặc sắp xếp lại giảm dần theo các sợi cáp trong cây khung và tăng dần theo các sợi cáp mới (tương tự như 2 heap) và sau đó sử dụng kỹ thuật two pointer.
#
# Độ phức tạp: O(MlogN + NlogN + QlogQ)O(MlogN+NlogN+QlogQ) trong đó MlogNMlogN là độ phức tạp Prim, NlogN + QlogQNlogN+QlogQ là độ phức tạp quá trình thay các cáp cũ bằng cáp mới.

import queue

INF = 1e9

class Node:
    def __init__(self, dist, index):
        self.dist = dist
        self.index = index

    def __lt__(self, other):
        return self.dist < other.dist

def prim(src):
    dist[src] = 0
    pq = queue.PriorityQueue()
    pq.put(Node(0, src))
    while not pq.empty():
        u = pq.get().index
        visited[u] = True
        for item in graph[u]:
            v, w = item.index, item.dist
            if not visited[v] and dist[v] > w:
                dist[v] = w
                pq.put(Node(dist[v], v))

    return dist

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
dist = [INF for i in range(n + 1)]
visited = [False for i in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append(Node(w, v))
    graph[v].append(Node(w, u))
mstCables = prim(1)[2: ]
mstCables.sort(reverse=True)
newCables = queue.PriorityQueue() # min heap
q = int(input())
if (q > 0):
    for cable in list(map(int, input().split())):
        newCables.put(cable)
res = 0
for oldCable in mstCables:
    usedCable = oldCable
    if not newCables.empty() and newCables.queue[0] < usedCable:
        usedCable = newCables.get()
    res += usedCable
print(res)
