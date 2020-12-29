# Với bài này, ta phải thử đi hết các đường đi từ nút gốc (nhà Kefa) đến tất cả nút lá (nhà hàng) để xem có bao nhiêu nút lá có thể đến được. Vậy ta sẽ sử dụng BFS để giải quyết bài này.

# Số đỉnh đánh dấu từ 11 nên khi lưu trữ dữ liệu và chạy BFS, ta cũng bắt đầu từ 11. Dùng một mảng chứa số lượng mèo xuất hiện khi đi từ đỉnh 11 đến đỉnh ii, đồng thời dùng một biến để đếm số nút lá (nhà hàng) có thể đến được.

# Đầu tiên ta phải xét liệu đỉnh 11 có chứa mèo, nếu có thì tăng số mèo ở đỉnh này lên 11.

# Kefa chỉ đi đến nhà hàng khi đường đó không xuất hiện quá MM con mèo, nên ta chỉ cần xét những đỉnh mà số lượng mèo xuất hiện nhỏ hơn hoặc bằng MM, lớn hơn MM không cần xét nữa.

# Vậy khi chạy BFS, thực hiện xét các đỉnh kề với đỉnh đang xét uu, nếu đỉnh kề vv chưa thăm thì đánh dấu đã thăm. Đồng thời, nếu đỉnh đó chứa mèo thì cập nhật lại cat[v] = cat[u] + 1, 
# và nếu cat[v]cat[v] nhỏ hơn hoặc bằng MM thì kiểm tra nếu số đỉnh kề với vv là 11 (đồng nghĩa với việc chỉ có 11 đỉnh đi đến đỉnh vv hay vv là nút lá) thì tăng biến đếm lên, ngược lại ta đẩy đỉnh vv vào hàng đợi.

import queue
 
MAX = 100000 + 5
cat = [0] * MAX
visited = [False] * MAX
graph = [[] for _ in range(MAX)]
 
def BFS(s):
    nrestaurants = 0
    q = queue.Queue()
    visited[s] = True
    q.put(s)
 
    cat[s] = (1 if a[s] == 1 else 0)
 
    while not q.empty():
        u = q.get()
 
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
             
                if a[v] == 1:
                    cat[v] = cat[u] + 1
                 
                if cat[v] <= m:
                    if len(graph[v]) == 1:
                        nrestaurants += 1
                    else:
                        q.put(v)
     
    return nrestaurants
 
n, m = map(int, input().split())
a = [None] + list(map(int, input().split()))
 
for i in range(1, n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
 
print(BFS(1))