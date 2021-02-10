# Đầu tiên bạn sẽ gắn toàn bộ đường đi một chiều vào đồ thị sau đó lần lượt gắn từng đường đi hai chiều vào, nếu đường nào cho ra đường đi ngắn nhất thì bạn chọn đó là kết quả cuối cùng.

# Lưu ý: Để làm được việc này thì mỗi lần gắn đường đi hai chiều vào bạn phải chạy lại thuật toán Dijkstra. Việc này sẽ làm bài bạn bị quá thời gian (TLE). Bạn phải cải tiến thuật toán Dijkstra và cải tiến luôn việc không thể gọi Dijkstra mỗi lần gắn đường đi hai chiều mới vào bằng cách sau:

# Tính Dijkstra từ SS \to→ TT và tính chiều ngược lại T \to ST→S (gọi Dijkstra hai lần).

# Sau khi chạy Dijkstra ta có:

# distS[u]: tìm đường đi từ đỉnh SS đến đỉnh uu (trong đồ thị bên dưới là 1 \to 51→5).
# distT[v]: tìm đường đi từ đỉnh vv đến đỉnh TT (trong đồ thị là 3 \to 43→4).
# Gắn từng đường đi hai chiều vào, lúc này dùng công thức bên dưới, công thức này giống như việc gọi Dijkstra lại mỗi lần gắn đường đi hai chiều vào.

# Sau khi gắn dd vào, nếu tổng này nhỏ hơn đường đi hiện tại đang có thì nó chính là đường đi ngắn nhất.

# int a = distS[u] + d + distT[v];
# int b = distS[v] + d + distT[u];
# result = min(result, min(a, b));
# Độ phức tạp: \mathcal {O} \left(T * E * log(V) \right)O(T∗E∗log(V)) với EE là số lượng cạnh của đồ thị, VV là số lượng đỉnh của đồ thị và TT là số lượng bộ test trong từng dữ liệu đầu vào.

from heapq import heappush, heappop
INF = 10 ** 9
MAX = 10001
 
def Dijkstra(s, dist, graph):
    pq = [(0, s)]
    dist[s] = 0
     
    while pq:
        w, u = heappop(pq)
         
        if w > dist[u]:
            continue
         
        for weight, v in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                heappush(pq, (dist[v], v))
 
T = int(input())
 
for _ in range(T):
    n, m, k, s, t = map(int, input().split())
     
    graphS = [[] for _ in range(MAX)]
    graphT = [[] for _ in range(MAX)]
    distT = [INF] * MAX
    distS = [INF] * MAX
     
    for i in range(m):
        u, v, d = map(int, input().split())
        graphS[u].append((d, v))
        graphT[v].append((d, u))
     
    Dijkstra(s, distS, graphS)
    Dijkstra(t, distT, graphT)
    res = distS[t]
     
    for i in range(k):
        u, v, d = map(int, input().split())
        res = min(res, distS[u] + d + distT[v], distS[v] + d + distT[u])
     
    print(res if res != INF else -1)