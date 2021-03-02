
# Bài này áp dụng BFS cơ bản, đọc vào số lượng đỉnh của đồ thị và danh sách cạnh. Sau đó chạy BFS bắt đầu từ điểm SS. Viết một hàm đếm các cạnh đi qua từ SS đến các đỉnh khác. Lấy kết quả đếm nhân 66 để ra kết quả cần tìm.

# Tuy nhiên ta có thể biến tấu thuật toán BFS đôi chút để có được kết quả ngay lúc duyệt đồ thị.

# Gọi dist[v]dist[v] lưu khoảng cách ngắn nhất từ đỉnh SS đến đỉnh vv. Với đỉnh vv có được thông qua duyệt các đỉnh kề của đỉnh uu. Như vậy dễ dàng nhận thấy dist[v] = dist[u] + 1, nghĩa là từ SS đến vv ta mất một quãng đường bằng khoảng cách từ SS đến uu và từ uu đến vv (chưa tính trọng số 66 của mỗi cạnh).

# Cuối cùng cho vòng lặp ii duyệt lại toàn bộ các đỉnh trong đồ thị. Nếu đỉnh đó chưa được viếng thăm thì in -1−1, ngược lại in dist[i]∗6 với trọng số của mỗi cạnh là 66.

# Độ phức tạp: O ( T * (V + E)) với T là số lượng test, V là số lượng đỉnh trong đồ thị và EE là số lượng cạnh trong đồ thị.


import queue

MAX = 1000 + 5
visited = [False] * MAX
dist = [0] * MAX
graph = [[] for i in range(MAX)]

def BFS(s):
    q = queue.Queue()
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                q.put(v)

Q = int(input())

for _ in range(Q):
    V, E = map(int, input().split())

    for i in range(MAX):        #reset graph
        graph[i].clear()
        visited[i] = False
        dist[i] = 0

    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    s = int(input())
    BFS(s)

    for i in range(1, V + 1):
        if i == s:
            continue

        print(dist[i] * 6 if visited[i] else -1, end=' ')

    print()