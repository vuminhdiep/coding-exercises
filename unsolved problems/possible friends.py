# Biến ma trận với các ký tự Y và N thành ma trận kề với hai người ii và jj là bạn của nhau sẽ có giá trị là 1, nếu ii bằng jj sẽ có giá trị là 0, còn lại gán giá trị là vô cực.
#
# Sử dụng thuật toán Floyd-Warshall tìm đường đi giữa tất cả các cặp đỉnh. Nếu cặp nào có giá trị là 2 nghĩa là người đó có 1 người có thể kết bạn. Sau khi đếm hết số lượng người có thể kết bạn của từng người, in ra người nào có số lượng gợi ý kết bạn nhiều nhất.


INF = 10 ** 9


def FloydWarshall():
    for k in range(M):
        for i in range(M):
            for j in range(M):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


T = int(input())

for _ in range(T):
    s = input()
    M = len(s)
    dist = [[INF] * M for i in range(M)]
    matrix = []

    for i in range(M):
        if i == 0:
            matrix.append(s)
        else:
            matrix.append(input())

        for j in range(M):
            if matrix[i][j] == 'Y':
                dist[i][j] = 1
            elif i == j:
                dist[i][j] = 0

    FloydWarshall()
    nfriends, index = 0, 0

    for i in range(M):
        count = 0

        for j in range(M):
            if dist[i][j] == 2:
                count += 1

        if count > nfriends:
            nfriends = count
            index = i

    print(index, nfriends)