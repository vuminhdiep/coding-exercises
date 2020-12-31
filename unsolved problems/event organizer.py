# Sử dụng thuật toán Floyd Warshall để giải quyết bài toán. • Xây dựng ma trận với dist[i][j]dist[i][j] là chi phí thu về lớn nhất trong thời gian từ i đến j. Nếu có nhiều sự kiện tổ chức cùng lúc thì chọn ra sự kiện có mức giá cao nhất. • Sau khi sử dụng Floyd Warshall, kết quả bài toán sẽ nằm trong dist[0][48]dist[0][48] tương ứng với chi phí thu về lớn nhất trong thời gian từ giờ thứ 00 đến giờ thứ 4848.
#
# Độ phức tạp: O(T * N^3) với T là số lượng bộ test, N là số lượng thời gian khác nhau (tức N = 49N=49 giờ khác nhau từ 00 đến 4848).

MAX = 48


def FloydWarshall():
    for k in range(MAX + 1):
        for i in range(MAX + 1):
            for j in range(MAX + 1):
                if i <= k <= j:
                    dist[i][j] = max(dist[i][j], dist[i][k] + dist[k][j])


T = int(input())
for _ in range(T):
    N = int(input())
    dist = [[0] * (MAX + 1) for i in range(MAX + 1)]

    for i in range(N):
        S, E, C = map(int, input().split())
        if C > dist[S][E]:
            dist[S][E] = C

    FloydWarshall()
    print(dist[0][MAX])