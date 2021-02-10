# Điều ta có thể kết luận ngay: Nếu tìm được một đường đi từ phòng số 11 \rightarrow→ nn có mức năng lượng dương \rightarrow→ in ra “winnable”.
#
# Tuy nhiên nếu ta không tìm được con đường như vậy, ta vẫn chưa thể kết luận điều gì vì có thể trên đường đi tồn tại một chu trình nào đó mà ta càng đi thì năng lượng sẽ càng tăng lên.
#
# Do đó bài này ta sẽ xử lý như sau:
#
# Dùng Bellman-Ford để tìm đường đi dài nhất từ 11 \rightarrow→ nn. Nếu khi đến phòng nn mà năng lượng dương thì in ra kết quả “winnable”.
# Ngược lại, duyệt qua các cạnh trong đồ thị.
# Nếu cạnh (u, v)(u,v) thuộc chu trình dương và từ uu có đường đi đến nn thì, không quan tâm mức năng lượng ta nhận thêm sau mỗi lần đi qua chu trình đó là bao nhiêu, điều chắc chắn là ta sẽ đi được đến nn với mức năng lượng dương, in kết quả “winnable”. \rightarrow→ Sử dụng BFS / DFS.
# Lưu ý: Để tìm đường đi dài nhất bằng Bellman-Ford, thay vì đặt khoảng cách từ đỉnh bắt đầu đến các đỉnh khác trong đồ thị là dương vô cực, ta đặt là âm vô cực.
#
# Độ phức tạp: độ phức tạp thuật toán Bellman Ford là O(V * E)O(V∗E). Với mỗi cạnh của đồ thị, ta có thể duyệt BFS lại một lần để kiểm tra chu trình thì độ phức tạp ở phần kiểm tra là O(E * (E + V))O(E∗(E+V)). Vậy độ phức tạp chung của cả chương trình là O(T * E * (E + V))O(T∗E∗(E+V)) với TT là số lượng bộ test đầu vào.

import queue

INF = 10 ** 9
energy = [0] * 105


class Edge:
    def __init__(self, _source, _target):
        self.source = _source
        self.target = _target


def hasPathBFS(s, f):
    visited = [False] * (n + 1)
    q = queue.Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()

        for edge in graph:
            if edge.source == u:
                v = edge.target

                if not visited[v]:
                    visited[v] = True
                    q.put(v)

                if v == f:
                    return True

    return False


def BellmanFord(s, f):
    dist = [-INF] * (n + 1)
    dist[1] = 100

    for i in range(n - 1):
        for edge in graph:
            u = edge.source
            v = edge.target
            if dist[u] > 0:
                dist[v] = max(dist[v], dist[u] + energy[v])

    for edge in graph:
        u = edge.source
        v = edge.target
        if dist[u] > 0 and dist[u] + energy[v] > dist[v] and hasPathBFS(u, f):
            return True

    return dist[f] > 0


while True:
    n = int(input())
    if n == -1:
        break

    graph = []

    for u in range(1, n + 1):
        line = list(map(int, input().split()))
        energy[u] = line.pop(0)

        if not line:  # input could be ill-formated
            line.extend(list(map(int, input().split())))

        m = line.pop(0)

        while len(line) != m:
            line.extend(list(map(int, input().split())))

        for v in line:
            graph.append(Edge(u, v))

    canGo = BellmanFord(1, n)
    print("winnable" if canGo else "hopeless")