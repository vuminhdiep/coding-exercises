# Giữa hai đỉnh (u, v)(u,v) có thể xảy ra 33 trường hợp:
#
# Tồn tại chu trình âm trên đường từ uu đến vv.
# Từ uu không thể đến vv.
# Từ uu đến được vv với đường đi ngắn nhất.
# Để kiểm tra lần lượt các trường hợp trên, ta sử dụng thuật toán Bellman-Ford.
#
# Trước tiên, ta sử dụng ma trận kề (adjacency matrix) hoặc danh sách cạnh (edge list) để lưu trọng số các cạnh (khuyến khích bạn lưu đồ thị dưới dạng danh sách cạnh để tránh lưu các thông tin thừa).
#
# Xây dựng danh sách cạnh của đồ thị:
# Nếu khoảng cách giữa 2 tượng đài khác nhau bằng 0, ta xem như không có cạnh nối và bỏ qua trường hợp này.
# Nếu khoảng cách giữa tượng đài đến chính nó là dương, ta xem như khoảng cách này bằng 0 (như đề bài đã nêu).
# Nếu khoảng cách giữa tượng đài đến chính nó bằng âm, đồng nghĩa với việc ta có thể đi nhiều lần từ đỉnh đó tới chính nó để độ dài đường đi giảm vô hạn, lúc này ta gán lại khoảng cách bằng âm vô cực.
# Sử dụng Bellman-Ford tìm đường đi ngắn nhất và phát hiện chu trình âm:
# Vì có nhiều truy vấn nên thay vì với mỗi truy vấn, ta chạy lại Bellman-Ford với mỗi đỉnh nguồn, ta có thể chạy Bellman-Ford với tất cả các đỉnh trong đồ thị duy nhất một lần và lưu kết quả vào mảng 2 chiều (mảng dist).
# Sau khi chạy thuật toán Bellmand-Ford từ mỗi đỉnh uu, ta cần kiểm tra lại và đánh dấu các đỉnh vv bị ảnh hưởng bởi chu trình âm (bằng cách gán dist[u][v] = -INF). Để đảm bảo tất cả các đỉnh bị ảnh hưởng bởi chu trình âm đều được đánh dấu, ta sẽ duyệt danh sách cạnh thêm N-1N−1 lần nữa.
# Với mỗi truy vấn, kiểm tra từng trường hợp nêu trên và in ra kết quả cần tìm.
#
# Độ phức tạp: O(T * (N^2 * M + Q) với TT là số test case, NN là số tượng đài – số đỉnh của đồ thị, MM là số cạnh tạo được bằng cách lưu danh sách cạnh, Q là số truy vấn.
#

INF = (1 << 30) * 100 + 7     # Should be large enough

def BellmanFord(s):
   dist[s][s] = 0

   for i in range(n - 1):
      for edge in graph:
         u, v, w = edge
         if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
            dist[s][v] = dist[s][u] + w

   for i in range(n - 1):
      for edge in graph:
         u, v, w = edge
         if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
            dist[s][v] = -INF

tc = 1
while True:
   n = int(input())
   if n == 0:
      break

   monuments = []
   graph = []
   dist = [[INF] * n for _ in range(n)]

   for i in range(n):
      name, *weights = input().split()
      monuments.append(name)
      for j in range(n):
         w = int(weights[j])
         if i != j and w == 0:
            continue
         if i == j and w >= 0:
            w = 0
         graph.append((i, j, w))

   for i in range(n):
      BellmanFord(i)

   print('Case #{}:'.format(tc))
   tc += 1
   q = int(input())

   for _ in range(q):
      u, v = map(int, input().split())
      if dist[u][v] <= -INF:		# Be careful here
         print('NEGATIVE CYCLE')
      else:
         print('{}-{} {}'.format(monuments[u], monuments[v], 'NOT REACHABLE' if dist[u][v] == INF else dist[u][v]))