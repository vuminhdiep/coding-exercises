# Ta có thể thấy rằng hai ô (x, y)(x,y) và ô (i, j)(i,j) sẽ đi được với nhau nếu chúng có chung cạnh. Do đó, nếu có thể xem mỗi ô trên ma trận là một đỉnh của một đồ thị, thì hai đỉnh trên đồ thị sẽ có một cạnh nối với nhau nếu chúng thỏa mãn ba tính chất sau đây:

# Hai ô được biểu diễn bởi hai đỉnh của đồ thị phải nằm trong phạm vi ma trận NNxMM.
# Hai ô, không ô nào được phép biểu diễn bởi số 00 (cả hai ô đều là số 11).
# Hai ô phải chung cạnh với nhau.
# Vì số lượng ô tối đa của một vũng dầu là NNxMM, nên để sắp xếp kích thước các vũng dầu theo thứ tự tăng dần và số vũng dầu của kích thước đó, ta chỉ cần tạo một mảng đếm NNxMM phần tử, sau đó chỉ cần duyệt từ 11 đến NNxMM và in số lượng vũng dầu có kích thước tương ứng.

# Như vậy, sau khi ta xây dựng được một đồ thị vô hướng, ý tưởng của ta sẽ như sau:

# Xác định vị trí của ô số 11, giả sử là ô (sx, sy)(sx,sy).
# Với mỗi ô (i, j)(i,j) trong ma trận mà được biểu diễn bằng số 11, ta sẽ sử dụng kỹ thuật duyệt DFS hoặc BFS từ ô (i, j)(i,j) để xem có thể đến được ô (sx, sy)(sx,sy) hay không, nếu có thì ta sẽ cập nhật kích thước của vũng dầu đó lên 11. Sau khi duyệt hết tất cả ô liền kề có số 11, ta cập nhật số lượng vũng dầu có kích thước tương ứng lên 11.
# Lưu ý: với Python để tăng tốc độ xử lý, ta tự cài đặt queue sử dụng trong thuật toán BFS bằng list với hai con trỏ leftleft để lấy phần tử đầu tiên và rightright để thêm phần tử vào cuối queue.

# Độ phức tạp:

# Time Complexity: \mathcal {O} \left (N * M \right )O(N∗M) với NN và MM lần lượt là độ dài của 22 cạnh của bảng.
# Space Complexity: \mathcal {O} \left (N * M \right )O(N∗M).

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
 
MAX = 251
table = [None] * MAX
slick = [0] * (MAX * MAX)
q = [None] * (MAX * MAX)
 
def BFS(sr, sc):
    left = right = 0
    q[0] = (sr, sc)
    table[sr][sc] = '0'
    count = 1
 
    while left <= right:
        ur, uc = q[left]
        left += 1
 
        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]
 
            if r in range(N) and c in range(M) and table[r][c] == '1':
                right += 1
                q[right] = (r, c)
                table[r][c] = '0'
                count += 1
 
    slick[count] += 1
 
while True:
    N, M = map(int, input().split())
 
    if N == 0 and M == 0:
        break
     
    for i in range(N):
        table[i] = input().split()
        for j in range(M):
            slick[i * M + j + 1] = 0
     
    nslicks = 0
 
    for i in range(N):
        for j in range(M):
            if table[i][j] == '1':
                nslicks += 1
                BFS(i, j)
     
    print(nslicks)
 
    for i in range(1, N * M  + 1):
        if slick[i]:
            print(i, slick[i], sep=' ')