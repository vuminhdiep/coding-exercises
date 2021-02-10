# Bài này khá đơn giản, bạn đọc tốt dữ liệu đầu vào, mỗi ví dụ bạn cần tìm đường đi ngắn nhất bằng thuật toán Dijkstra. Mỗi lần xong bạn sẽ in kết quả ra và xóa các tham số cần thiết trong graph, dist.

# Độ phức tạp: \mathcal {O} \left (Q * E * log(V) \right)O(Q∗E∗log(V)) với QQ là số lượng bộ test, EE là số lượng cạnh (cung) của đồ thị, VV là số lượng đỉnh của đồ thị.

from heapq import heappush, heappop
INF = 10 ** 9 + 7
 
def Dijkstra(s, f):
    global dist
    pq = [(0, s)]
    dist[s] = 0
     
    while pq:
        w, u = heappop(pq)
        if u == f:
            break
         
        if w > dist[u]:
            continue
         
        for weight, v in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                heappush(pq, (dist[v], v))
 
Q = int(input())
 
for t in range(1, Q + 1):
    n, m, S, T = map(int, input().split())
    graph = [[] for _ in range(n)]
     
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))
     
    dist = [INF] * n
    Dijkstra(S, T)
     
    print('Case #{}: '.format(t), end='')
    print(dist[T] if dist[T] != INF else "unreachable")