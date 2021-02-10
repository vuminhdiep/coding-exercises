# Nhận xét:

# Đồ thị chỉ có thể tồn tại chu trình chỉ khi nào có một cạnh nối từ uu đến một đỉnh vv nào đó được thăm trước đó, đồng thời từ vv phải đến được uu.
# Do đó ta cần thêm một mảng để truy vết đường đi và kiểm tra điều kiện trên, tạm gọi là mảng pathpath.
# Như vậy, ý tưởng giải cơ bản sẽ là sử dụng DFSDFS để duyệt qua từng đỉnh, với mỗi đỉnh uu đang xét, ta duyệt qua từng đỉnh vv kề với uu:

# Nếu vv chưa thăm thì ta duyệt DFS(v).
# Nếu vv thăm rồi, lúc này cần kiểm tra trong mảng path xem từ vv có đến được uu hay không, nếu đến được thì chứng tỏ có chu trình.
# Độ phức tạp: O(N)O(N) với mỗi đỉnh \rightarrow→ O(N^2)O(N
# ​2
# ​​ ) cho toàn đồ thị.

# Như vậy ta cần cải tiến để kiểm tra nhanh xem từ vv có đến được uu hay không.
# Nhận xét: Nếu từ vv đến được uu thì vv sẽ nằm trên đường đi từ gốc DFSDFS đến uu. Như vậy, nếu mình đánh dấu lại các đỉnh thuộc đường đi từ gốc đến uu, thì có thể kiểm tra nhanh vv có thuộc đường đi đó hay không, đồng nghĩa với việc từ vv có đến được uu hay không.
# Do đó thay vì dùng mảng pathpath, ta dùng một mảng là inPathinPath với inPath_i = trueinPath
# ​i
# ​​ =true nếu ii nằm trên đường đi từ gốc DFSDFS đến đỉnh uu đang xét, ngược lại inPath_i = falseinPath
# ​i
# ​​ =false.
# Khi mình duyệt xong DFS(u), thì lúc trở về đỉnh cha của uu, chắc chắn uu không nằm trên đường đi từ gốc đến cha của uu, nên cần gán lại inPath_u = falseinPath
# ​u
# ​​ =false trước khi thoát khỏi DFS(u).
# Ngoài ra, còn một cách xử lý nữa là sử dụng mảng visitedvisited, nhưng thay vì lúc này chỉ đánh dấu 0/1 (false/true)0/1(false/true) thì lúc này mình đánh dấu 33 giá trị nhằm mục đích sử dụng nó để thực hiện chức năng của cả 22 mảng visitedvisited và pathpath ở cách trên:

# visited_u = 0visited
# ​u
# ​​ =0 nếu uu chưa được duyệt (tức visited_u = falsevisited
# ​u
# ​​ =false và inPath_u = falseinPath
# ​u
# ​​ =false theo cách vừa trình bày).
# visited_u = 1visited
# ​u
# ​​ =1 nếu uu đã được duyệt và ta đang duyệt các đỉnh kề với u (visited_u = trueu(visited
# ​u
# ​​ =true và inPath_u = true)inPath
# ​u
# ​​ =true).
# visited_u = 2visited
# ​u
# ​​ =2 nếu uu đã được duyệt và đã duyệt xong các đỉnh kề với u (visited_u = trueu(visited
# ​u
# ​​ =true và inPath_u = false)inPath
# ​u
# ​​ =false).
# Độ phức tạp: O(V + E)O(V+E) với V, EV,E lần lượt là số lượng đỉnh và số lượng cạnh của đồ thị. Tuy nhiên, cách sử dụng mảng visited \ 3visited 3 giá trị sẽ ít tốn bộ nhớ hơn.

import sys
visited = [False] * 10005
graph = [[] for _ in range(10005)]
 
sys.setrecursionlimit(10005)
def DFS(u):
    visited[u] = 1
 
    for v in graph[u]:
        if visited[v] == 1:
            return True
        elif visited[v] == 0:
            if DFS(v):
                return True
     
    visited[u] = 2
    return False
 
T = int(input())
 
for _ in range(T):
    N, M = map(int, input().split())
 
    for i in range(N + 1):
        graph[i].clear()
        visited[i] = 0
     
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
     
    isCyclic = False
 
    for i in range(1, N + 1):
        if visited[i] == 0:
            isCyclic = DFS(i)
            if isCyclic:
                break
     
    print("YES" if isCyclic else "NO")