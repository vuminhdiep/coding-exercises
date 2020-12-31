# Ta thấy rằng giả sử từ loại tiền AA khi chuyển đổi sang loại tiền BB có tỉ giá là xx, và từ BB đổi sang CC có tỉ giá là yy thì khi đổi từ AA sang CC sẽ có tỉ giá là x \times yx×y.
#
# Mục tiêu của ta là tìm ra một cách quy đổi sao cho từ tỉ giá ban đầu tạo được lợi nhuận, tức là sẽ tạo thành 11 chu trình mà trong đó giá trị sẽ tăng lên sau khi thực hiện xong chu trình.
#
# Ứng dụng Floyd Warshall: ta xem mỗi loại tiền tệ là một đỉnh của đồ thị. Hai loại tiền tệ có thể quy đổi trực tiếp cho nhau thì sẽ có cạnh nối với trọng số là tỉ giá của cạnh, ngược lại thì trọng số bằng 00 (tức tỉ giá bằng 00, không thể quy đổi). Đồng thời, tỉ giá từ 11 loại tiền tệ ban đầu đến chính nó là 11.
#
# Chạy thuật toán Floyd Warshall, trong quá trình chạy thì ta sẽ cập nhật lại dist[i][j]dist[i][j] nếu dist[i][j]dist[i][j] nhỏ hơn dist[i][k] * dist[k][j]dist[i][k]∗dist[k][j].
#
# Mục tiêu cuối cùng của ta là sau khi thực hiện các phép chuyển đổi tiền tệ thì tỉ giá chuyển đổi từ 11 loại tiền tệ nào đó đến chính nó lớn hơn 11 (tức dist[i][i] > 1dist[i][i]>1) nghĩa là tồn tại một cách chuyển đổi từ loại tiền ii đi qua một loại tiền khác và quay về ii thì giá trị thu được của mình sẽ tăng so với ban đầu.

def FloydWarshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])


t = 1
while True:
    N = int(input())
    if N == 0:
        break

    dist = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    currencies = []

    for _ in range(N):
        currencies.append(input().strip())

    M = int(input())
    for _ in range(M):
        sourceCur, rate, desCur = input().split()
        u, v = map(lambda x: currencies.index(x), (sourceCur, desCur))
        dist[u][v] = float(rate)
    input()

    FloydWarshall()

    arbitrage = False
    for i in range(N):
        if dist[i][i] > 1:
            arbitrage = True
            break

    print('Case {}: {}'.format(t, "Yes" if arbitrage else "No"))
    t += 1
