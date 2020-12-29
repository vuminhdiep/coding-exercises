# Bạn có thể thấy rằng hai ô (x, y)(x,y) và ô (i, j)(i,j) sẽ đi được với nhau nếu chúng có chung cạnh. Do đó, nếu bạn có thể xem mỗi ô trên bảng là một đỉnh của một đồ thị, thì hai đỉnh trên đồ thị sẽ có một cạnh nối với nhau nếu chúng thỏa mãn ba tính chất sau đây:

# Hai ô được biểu diễn bởi hai đỉnh của đồ thị phải nằm trong bảng đầu vào.

# Hai ô, không ô nào được phép biểu diễn bởi ký tự ‘#’.

# Hai ô phải chung cạnh với nhau.

# Như vậy, sau khi ta xây dựng được một đồ thị vô hướng, cách đơn giản để giải quyết bài này là:

# Ta đi xác định vị trí của ô ‘@’, giả sử là ô (sx, sy)(sx,sy).

# Sau đó, với mỗi ô (i, j)(i,j) trong bảng được biểu diễn bằng dấu ‘..’, ta sẽ sử dụng kỹ thuật duyệt BFS/DFS từ ô (i, j)(i,j) để xác định xem có thể đến được ô (sx, sy)(sx,sy) hay không. Nếu có, ta tăng biến kết quả ansans lên 11.

# Kết quả là ans + 1ans+1 (Tính cả ô (sx, sy)(sx,sy)).

# Phải xét mỗi ô (i, j)(i,j) có đến được ô (sx, sy)(sx,sy) hay không như vậy khá tốn thời gian, ta có một cách khác để cải tiến thuật toán ở trên:

# Dựa vào một nhận xét tự nhiên, ta thấy mọi ô giả sử có đường đi đến ô (sx, sy)(sx,sy) thì chúng đều sẽ tập trung lại tại ô (sx , sy)(sx,sy). Do đó, nếu như ta nhìn nhận bài toán ở một khía cạnh khác, chúng ta sẽ phát hiện rằng: thay vì với mỗi ô (i , j)(i,j), ta kiểm tra xem có đường đi tới (sx, sy)(sx,sy), thì bây giờ ta sẽ xuất phát từ ô (sx , sy)(sx,sy), đi loang ra các đỉnh khác, mỗi lần ta tiếp cận được với một đỉnh mà chưa được xét thì ta sẽ tăng biến ansans lên 11 đơn vị. Kết quả là ansans.

# Độ phức tạp:

# Cách chưa cải tiến:

# Time Complexity: \mathcal {O} \left (T * W * W * H * H \right )O(T∗W∗W∗H∗H)

# Space Complexity: \mathcal {O} \left (W * H \right )O(W∗H)

# WW và HH không quá 2020 nên độ phức tạp \mathcal {O} \left (T * W * W * H * H \right )O(T∗W∗W∗H∗H) vẫn có thể chấp nhận được.

# Cách cải tiến:

# Time Complexity: \mathcal {O} \left (T * W * H \right )O(T∗W∗H) với WW và HH lần lượt là chiều rộng và chiều cao của bảng, còn TT là số lượng bộ test đầu vào.

# Space Complexity: \mathcal {O} \left (W * H \right )O(W∗H)

import queue
 
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
MAX = 21
visited = [[False] * MAX for _ in range(MAX)]
maze = [None] * MAX
 
class Cell:
    def __init__(self, _r, _c):
        self.r = _r
        self.c = _c
 
def isValid(r, c):
    return r in range(H) and c in range(W)
 
def BFS(s):
    q = queue.Queue()
    q.put(s)
    visited[s.r][s.c] = True
    count = 1
 
    while not q.empty():
        u = q.get()
 
        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]
 
            if isValid(r, c) and maze[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                q.put(Cell(r, c))
                count += 1
     
    return count
 
Q = int(input())
 
for k in range(1, Q + 1):
    W, H = map(int, input().split())
 
    for i in range(H):
        maze[i] = input()
     
    for i in range(H):    
        for j in range(W):
            if maze[i][j] == '@':
                s = Cell(i, j)
            visited[i][j] = False
 
    print("Case {}: {}".format(k, BFS(s)))