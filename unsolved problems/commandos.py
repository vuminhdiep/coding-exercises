# Để hoàn thành nhiệm vụ trong thời gian ngắn nhất, ta cần:

# Đặt bom trong thời gian ngắn nhất.
# Từ các tòa nhà di chuyển đến điểm tập trung tốn ít thời gian nhất.
# Vậy ta cần tìm đường từ tòa bắt đầu đến tất cả các tòa còn lại ngắn nhất có thể để đi đặt bom, dùng Dijkstra đi từ tòa bắt đầu.

# Đồng thời, cũng cần tìm đường ngắn nhất từ các tòa đến toà tập trung hay nói cách khác là từ tòa tập trung đến các các tòa còn lại, ta lại dùng Dijkstra đi từ tòa tập trung.

# Ta đã có đường đi ngắn nhất đến tất cả các đỉnh, đồng nghĩa với việc các tòa nhà đã bị đặt bom. Lính thì vô số, nên cho mỗi người từ tòa hiện tại phân đến các tòa lân cận tốn thời gian là như nhau, vậy thời gian để hoàn thành nhiệm vụ là dựa vào người đi lâu nhất. Do đó ta xét tại mỗi tòa nhà, đi từ tòa bắt đầu đến đó và từ đó đến tòa tập trung xem đường nào lâu nhất thì đó là thời gian ngắn nhất để hoàn thành nhiệm vụ.

from heapq import heappush, heappop
 
def Dijkstra(s):
    dist = [10 ** 9] * N
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
 
T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    R = int(input())
    graph = [[] for _ in range(N)]
     
    for _ in range(R):
        u, v = map(int, input().split())
        graph[u].append((1, v))
        graph[v].append((1, u))
     
    s, d = map(int, input().split())
    distS = Dijkstra(s)
    distD = Dijkstra(d)
    res = 0
     
    for i in range(N):
        res = max(res, distS[i] + distD[i])
     
    print("Case {}: {}".format(t, res))