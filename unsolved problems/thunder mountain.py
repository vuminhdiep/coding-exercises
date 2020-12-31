# Xem mỗi điểm là một đỉnh trong đồ thị, hai đỉnh có cạnh nối với nhau nếu như khoảng cách của nó không vượt quá 1010. Từ đồ thị tạo được chạy thuật toán Floyd Warshall để tìm độ dài đường đi ngắn nhất từ điểm 11 đến điểm nn.
#
# Lưu ý: Ta đặt khoảng cách dương vô cực lớn hơn giá trị của cặp đỉnh xa nhất là (0, 0) và (1024, 1024).

class Scanner:
    def __gen__():
        while True:
            buff = input().strip().split()
            for x in buff:
                yield x

    __sc__ = __gen__()

    def next():
        return Scanner.__sc__.__next__()


INF = 1029
MAX = 105
x = [None] * MAX
y = [None] * MAX
dist = [[0] * MAX for _ in range(MAX)]


def getDistance(i, j):
    return ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5


def FloydWarshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


N = int(Scanner.next())

for t in range(1, N + 1):
    n = int(Scanner.next())

    for i in range(n):
        for j in range(n):
            dist[i][j] = (0 if i == j else INF)

    for i in range(n):
        x[i] = int(Scanner.next())
        y[i] = int(Scanner.next())

    for i in range(n):
        for j in range(n):
            d = getDistance(i, j)
            if d <= 10:
                dist[i][j] = d

    FloydWarshall()

    res = 0
    for i in range(n):
        for j in range(n):
            res = max(res, dist[i][j])

    print('Case #{}:'.format(t))
    print(res if res != INF else 'Send Kurdy')
    print()