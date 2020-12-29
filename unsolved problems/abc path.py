# Ta có thể nhận thấy rằng việc duyệt A, rồi sau đó duyệt tìm đến B, C, v.v. giống như duyệt theo độ sâu bảng chữ cái dựa trên các chữ cái trong bảng, như vậy ta có thể áp dụng DFS cho bài toán này. Do đường đi cần tìm chỉ có thể bắt đầu từ ‘A’ nên ta sẽ duyệt qua từng phần tử trong bảng, nếu nó là ký tự ‘A’ ta sẽ bắt đầu thực hiện DFS từ đây, trong giải thuật DFS cần chú ý các điểm sau:

# Để đi qua các điểm liền kề điểm hiện tại (ngang, dọc, chéo) phải thỏa điều kiện: ký tự mới phải liền sau ký tự hiện tại (ví dụ ký tự hiện tại là C thì ký tự kế tiếp phải là D). Ta có thể kiểm tra bằng việc so sánh mã ASCII ký tự sau = mã ASCII ký tự trước + 1.
# Trong lúc duyệt DFS ta phải lồng ghép vào đếm độ sâu của phép duyệt này được bao nhiêu ký tự. Số lượng lớn nhất trong các lần duyệt chính là kết quả bài toán.
# Độ phức tạp: O(n * m)O(n∗m) với n, m lần lượt là kích thước của bảng. Khi sử dụng mảng visited chung cho các lần duyệt dfs thì mỗi ô chỉ đc duyệt tối đa 1 lần.

import sys
sys.setrecursionlimit(10000000)

DIR = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

case = 0
while True:
    case += 1
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    a = []
    for i in range(h):
        a.append(input())
    dist = [[0] * w for i in range(h)]

    def find_path(u, v):
        if dist[u][v]:
            return dist[u][v]
        max_path = 0
        for dx, dy in DIR:
            n_u, n_v = u + dx, v + dy
            if n_u < 0 or n_u >= h or n_v < 0 or n_v >= w or ord(a[n_u][n_v]) != ord(a[u][v]) + 1:
                continue
            max_path = max(max_path, find_path(n_u, n_v))
        dist[u][v] = max_path + 1
        return dist[u][v]

    res = 0
    for x in range(h):
        for y in range(w):
            if a[x][y] == 'A':
                res = max(res, find_path(x, y))
    print('Case {}: {}'.format(case, res))