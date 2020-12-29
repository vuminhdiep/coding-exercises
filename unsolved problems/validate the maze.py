# Cách 1:

# Bạn sẽ chuyển toàn bộ đồ thị đã cho về ma trận kề hoặc danh sách kề, bằng cách duyệt qua toàn bộ ma trận, hai đỉnh được nối với nhau khi và chỉ khi có thể đi từ “.” này đến “.” kia.

# Bạn có thể đặt đỉnh ở tọa độ (0, 0)(0,0) là đỉnh 00, (0, 1)(0,1) là đỉnh 11, … lần lượt như vậy. Nếu đồ thị có 44x44 thì bạn sẽ có 1616 đỉnh ((từ 00 đến 1515)).

# Bước tiếp theo bạn sẽ xem đỉnh nào ở rìa ma trận thì sẽ đặt đỉnh đó là đỉnh vào hoặc đỉnh ra, bạn cần tìm đủ 22 đỉnh như vậy rồi chạy BFS. Nếu có đường đi thì bạn sẽ in ra “validvalid” ngược lại bạn sẽ in ra “invalidinvalid”.

# \to→ Nhận xét: Với cách giải này bạn sẽ tốn thời gian chuẩn bị lại đồ thị cho đúng định dạng.

# Cách 2:

# Bạn sẽ chạy BFS trên mê cung đã cho mà không cần phải chuyển lại thành dạng ma trận kề hay danh sách kề. Cách này bạn phải thêm và chỉnh lại một số dòng code để chạy phù hợp.

# Ban đầu, bạn cũng sẽ tìm hai điểm đầu vào và đầu ra. Từ điểm đầu ra bạn sẽ xác định 44 hướng đi (lên, xuống, trái, phải). 
# Nếu có đường đi, nghĩa là gặp dấu “.” và nằm trong giới hạn của mê cung thì bạn sẽ dịch chuyển bước đi của mình xuống điểm mới. Lần lượt đi đến khi nào gặp đỉnh đầu ra thì dừng.
#  Lúc này sẽ in ra là “valid”, ngược lại nếu đi mà không thấy đường ra sẽ in ra “invalid”.

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
    return r in range(n) and c in range(m)
 
def BFS(s, f):
    q = queue.Queue()
    visited[s.r][s.c] = True
    q.put(s)
 
    while not q.empty():
        u = q.get()
        if u.r == f.r and u.c == f.c:
            return True
 
        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]
 
            if isValid(r, c) and maze[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                q.put(Cell(r, c))
     
    return False
 
Q = int(input())
 
for _ in range(Q):
    n, m = map(int, input().split())
 
    for i in range(n):
        maze[i] = input()
     
    entrance = []
 
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            if maze[i][j] == '.' and (i == 0 or j == 0 or i == n - 1 or j == m - 1):
                entrance.append(Cell(i, j))
     
    if (len(entrance)) != 2:
        print("invalid")
    else:
        s = entrance[0]
        f = entrance[1]
        print("valid" if BFS(s, f) else "invalid")