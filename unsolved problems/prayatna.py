# Lần lượt chạy DFSDFS cho các đỉnh, nếu mỗi lần chạy vẫn còn đỉnh nào có giá trị falsefalse nghĩa là vẫn còn nhóm nào đó khác nhóm trước đã chạy. Bạn sẽ tăng biến đếm lên. Khi chạy hết NN đỉnh thì kết quả cuối cùng là biến đếm.

def DFS(src):
    s = [src]
    visited[src] = True

    while len(s):
        u = s.pop()
        
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)
    
Q = int(input())

for _ in range(Q):
    line = ''
    while line == '':
        line = input().strip()

    V = int(line)
    E = int(input())
    graph = [[] for _ in range(V)]
    visited = [False] * V

    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    count = 0

    for i in range(V):
        if not visited[i]:
            count += 1
            DFS(i)
    
    print(count)