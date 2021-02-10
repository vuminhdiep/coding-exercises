# Lưu ý: Bài tập này có thể được giải bằng cả ba thuật toán tìm đường đã học: Dijkstra, Bellman Ford và Floyd Warshall. Tuy nhiên với mỗi bộ test, ta lại có nhiều truy vấn. Do đó sẽ rất bất tiện nếu sử dụng Dijkstra hay Bellman Ford vì với mỗi truy vấn, ta phải chạy lại thuật toán. Floyd Warshall chính là lựa chọn rất tốt để giải quyết vấn đề trên.
#
# Về việc áp dụng Floyd Warshall trong bài tập này, ta cần lưu ý:
#
# Chi phí đi từ uu đến vv lúc này không chỉ bằng tổng trọng số các cạnh trên đường đi đã chọn mà còn phụ thuộc vào chi phí của đỉnh lớn nhất trong đường đi.
# \Rightarrow⇒ Dùng thêm ma trận maxCostmaxCost với maxCost[i][j]maxCost[i][j] là chi phí của đỉnh lớn nhất trên đường đi nhỏ nhất từ ii đến jj.
# Khi này, đường đi từ ii đến đỉnh trung gian kk, rồi từ đỉnh trung gian kk đến jj có thể tính bằng công thức: dist[i][k] + dist[k][j] + max(maxCost[i][k], maxCost[k][j])dist[i][k]+dist[k][j]+max(maxCost[i][k],maxCost[k][j]).
#
# Ta đem so sánh đường qua đỉnh trung gian kk với đường đi hiện tại từ ii đến jj là dist[i][j] + maxCost[i][j]dist[i][j]+maxCost[i][j]. Nếu tốt hơn thì cập nhật lại cả độ dài đường đi ngắn nhất và giá trị trong maxCostmaxCost.
#
# Lưu ý: Với bài này, hai đại lượng là distdist và maxCostmaxCost có thể ảnh hưởng qua lại lẫn nhau (distdist tính theo maxCostmaxCost, còn maxCostmaxCost thì chỉ được cập nhật khi distdist thay đổi) nên để đảm bảo rằng cả hai đại lượng đều tối ưu, ta phải duyệt Floyd 22 lần.
#
# Độ phức tạp: O(T * C^3)
# với T là số lượng bộ test, C là số thành phố trong mỗi test case.

maxCost = [[None] * 85 for _ in range(85)]
INF = 10 ** 9
t = 1


def FloydWarshall():
    for _ in range(2):
        for k in range(1, C + 1):
            for i in range(1, C + 1):
                for j in range(1, C + 1):
                    maxFeast = max(maxCost[i][k], maxCost[k][j])
                    if dist[i][j] + maxCost[i][j] > dist[i][k] + dist[k][j] + maxFeast:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        maxCost[i][j] = maxFeast


while True:
    C, R, Q = map(int, input().split())

    if C == 0:
        break

    f = [0] + list(map(int, input().split()))

    for i in range(1, C + 1):
        for j in range(1, C + 1):
            maxCost[i][j] = max(f[i], f[j])

    dist = [[INF] * (C + 1) for _ in range(C + 1)]

    for _ in range(R):
        u, v, w = map(int, input().split())
        dist[u][v] = dist[v][u] = w

    FloydWarshall()

    if t > 1:
        print()

    print('Case #{}'.format(t))
    t += 1

    for _ in range(Q):
        u, v = map(int, input().split())
        print(-1 if dist[u][v] == INF else dist[u][v] + maxCost[u][v])