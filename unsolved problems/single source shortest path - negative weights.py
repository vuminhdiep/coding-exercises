# Hướng dẫn giải:
#
# Nhận xét: Nhiệm vụ của ta là tìm đường đi ngắn nhất từ một đỉnh đến các đỉnh còn lại trên đồ thị có cạnh có trọng số âm, do đó ta sẽ áp dụng thuật toán Bellman-Ford để giải quyết.
#
# Sau khi chạy Bellman-Ford một lần để lấy được trọng số nhỏ nhất từ đỉnh nguồn đến các đỉnh còn lại trong đồ thị. Lúc này xét các khoảng cách thu được:
#
# Nếu khoảng cách từ đỉnh nguồn ss tới đỉnh ii có giá trị là dương vô cực, nghĩa là không tồn tại đường đi từ ss \rightarrow→ ii.
# Ngược lại, nếu khoảng cách này khác dương vô cực có thể xảy ra 22 trường hợp:
# Đó là trọng số nhỏ nhất đi từ ss \rightarrow→ ii.
# Đỉnh ii thuộc chu trình âm nên khảng cách này là không xác định.
# Ta biết rằng thuật toán Bellman-Ford truyền thống chỉ cho phép ta pháp hiện có tồn tại chu trình âm bất kỳ trong đồ thị chứ không chỉ rõ các đỉnh thuộc các chu trình âm trong đồ thị đó. \rightarrow→ Chạy Bellman-Ford lần hai, nếu lại tìm được một khoảng cách từ ss \rightarrow→ vv tốt hơn thì chắc chắn vv thuộc chu trình âm. Ta gán khoảng cách là âm vô cực.
#
# Cuối cùng với mỗi truy vấn, ta gọi đỉnh yêu cầu uu và so sánh:
#
# Nếu khoảng cách từ ss \rightarrow→ uu là dương vô cực: in “Impossible”.
# Nếu khoảng cách từ ss \rightarrow→ uu là âm vô cực: in “-Infinity”.
# Ngược lại, khoảng cách từ ss \rightarrow→ uu xác định, ta in ra khoảng cách ấy.
# Độ phức tạp: Ta sẽ phải chạy thuật Bellman-Ford 22 lần cho mỗi bộ test tốn O(n * m)O(n∗m) và đọc dữ liệu tốn O(m + q)O(m+q). Vậy độ phức tạp toàn bài là O(T * n * m)O(T∗n∗m) với TT là số lượng bộ test, nn là số đỉnh và mm là số cạnh của đồ thị.


INF = 10 ** 9


def BellmanFord(s):
    dist[s] = 0

    for i in range(n - 1):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for i in range(n - 1):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF


while True:
    n, m, q, s = map(int, input().split())

    if n == 0:
        break
    graph = []

    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))

    dist = [INF] * n
    BellmanFord(s)

    for _ in range(q):
        f = int(input())

        if dist[f] == INF:
            print("Impossible")
        elif dist[f] == -INF:
            print("-Infinity")
        else:
            print(dist[f])
    print()