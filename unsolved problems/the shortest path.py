# Bỏ các tên thành phố vào một mảng danh sách các thành phố (mảng chuỗi). Sau đó bỏ lần lượt từng đường đi vào graph bình thường. Khi tìm đường đi giữa 22 thành phố với nhau chỉ cần tìm lại index của thành phố đó ban đầu khi bỏ vào mảng thành phố là xong.

# Độ phức tạp: \mathcal {O} \left(s * p * E * log(V) \right)O(s∗p∗E∗log(V)) với ss là số lượng bộ test, pp là số lượng truy vấn tìm đường đi ngắn nhất giữa 22 thành phố, EE là số lượng cạnh (cung) của đồ thị và VV là số lượng đỉnh của đồ thị trong mỗi bộ test.

from heapq import heappush, heappop
 
def Dijkstra(s, f):
    dist = [10 ** 9] * (N + 1)
    pq = [(0, s)]
    dist[s] = 0
     
    while pq:
        w, u = heappop(pq)
         
        if u == f:
            break
         
        for weight, v in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                heappush(pq, (dist[v], v))
     
    return dist[f]
     
T = int(input())
 
for t in range(T):
    N = int(input())
    graph = [[] for i in range(N + 1)]
    cities = []
     
    for u in range(1, N + 1):
        name = input()
        cities.append(name)
        neighbors = int(input())
         
        for i in range(neighbors):
            v, w = map(int, input().split())
            graph[u].append((w, v))
     
    Q = int(input())
     
    for i in range(Q):
        sCity, fCity = input().split()
        s = cities.index(sCity) + 1
        f = cities.index(fCity) + 1
        print(Dijkstra(s, f))
     
    input()