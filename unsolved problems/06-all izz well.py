# Để kiểm tra xem có đường đi nào tạo thành chuỗi ALLIZZWELL hay không, ta sẽ thực hiện chạy DFSDFS từ tất cả các ô chứa ký tự A - ký tự bắt đầu của chuỗi đề cho. Với mỗi bước đi, ta chọn các ô có chứa ký tự tiếp theo trong chuỗi ALLIZZWELL. Nếu đạt tới ký tự cuối cùng trong chuỗi nghĩa là ta đã có một đường đi hợp lệ tạo thành chuỗi đề cho.

# Ta lưu ý rằng nếu có bất cứ ô nào thỏa điều kiện là ký tự kế tiếp trong chuỗi, ta chưa thể kết luận là toàn bộ đường đi đó không thể tạo thành chuỗi ALLIZZWELL, hay nói cách khác là ta không thể duyệt qua một lần đỉnh uu và đánh dấu visited_u = truevisited
# ​u
# ​​ =true.

# Chẳng hạn nếu ta đã tìm được một đường đi A \rightarrow L \rightarrow L \rightarrow I \rightarrow Z \rightarrow Z \rightarrow WA→L→L→I→Z→Z→W nhưng ô tiếp theo ta xét lại là ô có ký tự L - không giống ký tự ta mong đợi là E. Tuy nhiên ta cần hiểu rằng ta không thể loại bỏ ký tự L này được vì rất có thể về sau khi ta đã tìm được một đường đi A \rightarrow L \rightarrow L \rightarrow I \rightarrow Z \rightarrow Z \rightarrow W \rightarrow EA→L→L→I→Z→Z→W→E thì ký tự L đó có thể là một đỉnh hợp lệ trong đường đi của ta.

# Do đó, ta sẽ sử dụng kỹ thuật Backtracking (quay lui) như sau:

# Với mỗi đỉnh u = s_iu=s
# ​i
# ​​ , ta đánh dấu uu là một đỉnh trong đường đi visited_u = truevisited
# ​u
# ​​ =true.
# Chạy DFSDFS từ ký tự i + 1i+1 về sau.
# Đánh dấu lại visited_u = falsevisited
# ​u
# ​​ =false để tái sử dụng (nếu có thể) trong những đường đi khác.
# Độ phức tạp: O(t*R*C)O(t∗R∗C) với tt là số lượng bộ test, R, Ctest,R,C là số dòng và số cột của từng ma trận trong mỗi testcasetestcase.

import sys
sys.setrecursionlimit(100000)

dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, 1, -1, 0, 1, -1]
term = "ALLIZZWELL"

def DFS(sr, sc, count):
    global found, table, visited
    if count == len(term):
        found = True
        return
    
    for i in range(8):
        r = sr + dr[i]
        c = sc + dc[i]

        if r in range(R) and c in range(C) and table[r][c] == term[count] and not visited[r][c]:
            visited[r][c] = True
            DFS(r, c, count + 1)
            visited[r][c] = False
    
T = int(input())

for _ in range(T):
    R, C = map(int, input().split())
    table = []
    visited = [[False] * C for _ in range(R)]

    for i in range(R):
        table.append(input())
    
    found = False

    for i in range(R):
        for j in range(C):
            if table[i][j] == term[0] and not found:
                DFS(i, j, 1)
    
    print("YES" if found else "NO")
    input()