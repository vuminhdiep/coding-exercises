# Bạn sẽ sử dụng thuật toán Dijkstra để tìm đường đi ngắn nhất từ A đến mọi thành phố và từ B đến mọi thành phố.

# Gọi distA[i]distA[i] là khoảng cách ngắn nhất từ AA đến 1 thành phố ii bất kỳ.
# Gọi distB[i]distB[i] là khoảng cách ngắn nhất từ BB đến 1 thành phố ii bất kỳ.
# Như vậy bạn sẽ duyệt qua kk thành phố có bán chocolate và tìm min trong tổng khoảng cách từ AA đến thành phố đó và BB đến thành phố đó.

# Một điều cần chú ý là khoảng cách từ BB đến thành phố bán chocolate không được vượt quá xx vì như vậy chocolate sẽ tan. Do bài này test khá lớn, nên cần lưu ý việc nhập/xuất dữ liệu. Đồng thời, trong thuật Dijkstra, khi gặp một khoảng cách tốt hơn/đường đi ngắn hơn thì thì lưu lại khoảng cách đó dist[v] = wdist[v]=w và cặp (w, v)(w,v) được thêm vô hàng đợi. Vậy thì những cặp đã thêm vô hàng đợi trước đó có cùng đỉnh vv, chắc chắn khoảng cách đi kèm sẽ lớn hơn ww của cặp vừa thêm vào. Nên bạn có thể bỏ qua những cặp đó (w > dist[v])(w>dist[v]) không cần xét.

# Độ phức tạp: O(ElogV)O(ElogV) với EE là số lượng cạnh (cung) của đồ thị, VV là số lượng đỉnh của đồ thị.

from heapq import heappush, heappop
INF = 10 ** 9

def Dijkstra(s):
	dist = [INF] * (N + 1)
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
	
	return dist

N, M, k, x = map(int, input().split())
cities = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
	u, v, d = map(int, input().split())
	graph[u].append((d, v))
	graph[v].append((d, u))

A, B = map(int, input().split())

distA = Dijkstra(A)
distB = Dijkstra(B)
res = INF

for city in cities:
	if distB[city] <= x:
		res = min(res, distA[city] + distB[city])
	
print(res if res < INF else -1)