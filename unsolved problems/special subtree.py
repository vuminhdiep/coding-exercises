# Từ điều kiện 33 ta có thể suy ra đồ thị con này phải là 11 cây (vì chỉ có cây mới có chính xác 11 đường đi giữa mọi cặp đỉnh trong cây).
#
# Từ điều kiện 11, kết hợp cũng điều kiện 33 ở trên thì suy ra đây là một cây khung của đồ thị (cây chứa toàn bộ các đỉnh của đồ thị). Kết hợp cùng điều kiện 22, suy ra đây là bài toán tìm cây khung nhỏ nhất của đồ thị.
#
# Đối với bài này, ta đơn giản chỉ cần chạy giải thuật Prim bắt đầu từ điểm SS mà đề đã cho để tìm cây khung nhỏ nhất của đồ thị (cũng chính là đồ thị con theo như yêu cầu của đề). Một lưu ý đặc biệt là trong dữ liệu nhập vào có thể có cùng một cạnh nối hai đỉnh nhưng trọng số khác nhau, và cả hai cạnh này đều được xem như là hai cạnh hợp lệ của đồ thị. Nhưng theo cách chạy giải thuật Prim thì ta chỉ cần một cạnh là đủ, vậy ta sẽ giải quyết vấn đề này bằng cách mỗi khi thêm cạnh mới vào mảng Graph, ta kiểm tra xem đã tồn tại cạnh nối hai đỉnh này chưa, nếu rồi thì ta xem thì liệu giữa hai cạnh thì cạnh nào có trọng số nhỏ hơn ta lấy, còn nếu chưa tồn tại thì ta thêm vô bình thường. Một lưu ý khác là dữ liệu có thể lớn nên sử dụng biến kiểu 6464-bit sẽ tốt hơn.
#
# Độ phức tạp: O(MlogN)O(MlogN)


import queue

INF = 10 ** 9


class node:
    def __init__(self, dist, index):
        self.dist = dist
        self.index = index

    def __lt__(self, other):
        return self.dist < other.dist

    def __str__(self):
        return "%d %d" % (self.index, self.dist)


def prim(graph, src):
    n = len(graph)
    dist = [INF] * n
    path = [-1] * n
    visited = [False] * n
    dist[src] = 0
    visited[src] = True

    Q = queue.PriorityQueue()
    Q.put(node(0, src))

    while not Q.empty():
        u = Q.get().index
        visited[u] = True
        for nxt in graph[u]:
            v, w = nxt.index, nxt.dist
            if not visited[v] and dist[v] > w:
                dist[v] = w
                Q.put(node(dist[v], v))
                path[v] = u

    total_cost = 0
    for i in range(n):
        if path[i] != -1:
            total_cost += dist[i]

    return total_cost


n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append(node(w, v - 1))
    graph[v - 1].append(node(w, u - 1))

s = int(input())
print(prim(graph, s - 1))