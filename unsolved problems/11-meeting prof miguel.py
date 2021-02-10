# Đề không đảm bảo từ thành phố này đến thành phố kia chỉ có một đường nối trực tiếp. Vậy nên dữ liệu có thể lặp lại (có thể có nhiều đường nối trực tiếp giữa hai thành phố). Khi đó, bạn phải chọn dữ liệu nhỏ nhất, như ví dụ bên dưới bạn sẽ chọn trọng số 1010 thay vì 100100:
#
# Y U A B 10
# Y U A B 100
#
# Từ dữ liệu đề cho bạn tạo ra hai bản đồ riêng cho Shahriar và Miguel. Sau đó sử dụng Dijkstra hoặc Floyd-Warshall để tìm đường đi ngắn nhất cho bản đồ của cả hai.
#
# Sau đó lọc ra các địa điểm mà cả hai có thể đến được và chọn ra những địa điểm mà tổng đường đi của cả hai có chi phí thấp nhất. In ra theo yêu cầu của đề bài.


INF = 10 ** 9
MAX = 28


def FloydWarshall(dist):
    for k in range(MAX):
        for i in range(MAX):
            for j in range(MAX):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


while True:
    N = int(input())
    if N == 0:
        break

    distS = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]
    distD = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]

    for _ in range(N):
        age, dir, x, y, c = input().split()
        u, v = map(lambda char: ord(char) - ord('A'), (x, y))
        c = int(c)

        if age == 'Y':
            distS[u][v] = min(distS[u][v], c)
            if dir == 'B':
                distS[v][u] = min(distS[v][u], c)
        else:
            distD[u][v] = min(distD[u][v], c)
            if dir == 'B':
                distD[v][u] = min(distD[v][u], c)

    s, d = map(lambda char: ord(char) - ord('A'), input().split())
    FloydWarshall(distS)
    FloydWarshall(distD)

    res = []
    minDist = INF

    for i in range(MAX):
        dist1 = distS[s][i]
        dist2 = distD[d][i]

        if dist1 != INF and dist2 != INF and dist1 + dist2 <= minDist:
            res.append((dist1 + dist2, i))
            minDist = dist1 + dist2

    if not res:
        print('You will never meet.')
    else:
        res.sort()
        print(minDist, end='')

        for place in res:
            if place[0] != minDist:
                break
            print(' ' + chr(place[1] + ord('A')), end='')
        print()