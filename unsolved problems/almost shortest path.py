# Nhận xét: Để được đường đi gần ngắn nhất, ta cần một đồ thị không bao gồm các cạnh chứa trong những đường đi ngắn nhất và chạy Dijkstra trên đồ thị mới. Do đó mục tiêu của ta là phải loại bỏ các cạnh này ra khỏi đồ thị ban đầu, hay nói cách khác là kiểm tra một cạnh có thuộc bất kỳ đường đi ngắn nhất nào hay chưa để quyết định đưa vào đồ thị mới.
# Đầu tiên ta sẽ chạy Dijkstra 2 lần từ SS và từ DD để lưu lại đường đi ngắn nhất từ đỉnh SS và DD đến một đỉnh i bất kỳ trong đồ thị.

# Sau khi chạy xong, ta sẽ được độ dài đường đi ngắn nhất từ S \rightarrow DS→D là distS[D]distS[D].

# Lần lượt duyệt qua từng đỉnh uu trong đồ thị, kiểm tra xem cách đỉnh kề vv của uu có chi phí là ww có thuộc đường đi ngắn nhất bằng cách so sánh tổng (distS[u] + w + distD[v])(distS[u]+w+distD[v]) với độ dài đường đi ngắn nhất vừa tìm được.

# Nếu bằng nghĩa là cạnh (u, v, w)(u,v,w) thuộc đường đi ngắn nhất, ta bỏ qua cạnh đó.
# Ngược lại ta đưa cạnh (u, v, w)(u,v,w) vào đồ thị mới.
# Cuối cùng chỉ cần chạy Dijkstra trên đồ thị mới là ta sẽ có đường đường đi gần ngắn nhất không bao gồm các cạnh thuộc đường đi ngắn nhất.

from heapq import heappush, heappop
INF = 10 ** 9
MAX = 505

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

while True:
	N, M = map(int, input().split())
	
	if N == 0 and M == 0:
		break
	
	graph = [[] for _ in range(N)]
	graphS = [[] for _ in range(N)]
	graphD = [[] for _ in range(N)]
	dist = [INF] * N
	distS = [INF] * N
	distD = [INF] * N
		
	S, D = map(int, input().split())
	
	for i in range(M):
		u, v, w = map(int, input().split())
		graphS[u].append((w, v))
		graphD[v].append((w, u))
	
	Dijkstra(S, distS, graphS)
	Dijkstra(D, distD, graphD)
	shortestPath = distS[D]
	
	for u in range(N):
		for w, v in graphS[u]:
			if distS[u] + w + distD[v] != shortestPath:
				graph[u].append((w, v))
	
	Dijkstra(S, dist, graph)
	print(dist[D] if dist[D] != INF else -1)