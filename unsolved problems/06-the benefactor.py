# Xem danh sách được cho là một đồ thị với các đỉnh là các địa điểm trong thị trấn và con đường nối giữa hai địa điểm là một cạnh của đồ thị. Ta có:

# Giữa hai đỉnh bất kì luôn chỉ có một cạnh nối -− đồ thị dạng cây (E = V – 1).
# Độ dài lớn nhất giữa hai đỉnh bất kì chính là đường kính của cây.
# Như vậy bài toán của ta trở thành bài toán tìm đường kính của cây. Ta lại có nhận xét đường kính của cây chính là khoảng cách lớn nhất giữa hai node lá. Như vậy nhiệm vụ của mình là phải tìm hai node lá này.

# Giả sử ta thực hiện DFS từ một đỉnh bất kì. Điều chắn chắn rằng node có khoảng cách xa nhất từ điểm mà ta bắt đầu lan chính là một node lá cần tìm. Khi này chỉ cần sử dụng tiếp DFS để đi từ node lá mới tìm được là ta sẽ có được node lá thứ hai, đồng thời tính được khoảng cách giữa hai node lá đó, tức đường kính của cây. Thuật toán này có tên là “Double DFS” được mở rộng từ thuật toán DFS cơ bản.

# Tóm lại, bài này ta có thể thực hiện như sau:

# Bước 1: Đọc dữ liệu. Biết số cạnh = số đỉnh – 1 (tính chất của cây).
# Bước 2: Khởi tạo biến lưu khoảng cách xa nhất từ node mà ta đang xét là max_dist = 0. Khai báo biến leaf lưu node lá.
# Bước 3: Chạy DFS từ một đỉnh bất kì. Nếu tìm được đỉnh v có khoảng cách đến điểm bắt đầu lớn hơn max_dist:
# Cập nhật max_dist = dist[v]
# Cập nhật node lá leaf = v
# Bước 4: Chạy DFS từ đỉnh f. Nếu tìm được đỉnh v có khoảng cách đến điểm bắt đầu lớn hơn max_dist thì cập nhật max_dist = dist[v].
# Bước 5: In ra kết quả trong max_dist.
# Độ phức tạp: O(T * (V + E))O(T∗(V+E)) với VV là số lượng đỉnh và EE là số lượng cạnh của đồ thị và TT là số lượng bộ test cho mỗi dataset

def DFS(src):
    global leaf, max_dist
    dist = [-1] * (V + 1)
    s = [src]
    dist[src] = 0

    while len(s):
        u = s.pop()

        for v, w in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + w
                max_dist = max(max_dist, dist[v])
                s.append(v)
    
    leaf = dist.index(max(dist))

t = int(input())

for _ in range(t):
    V = int(input())
    E = V - 1
    graph = [[] for _ in range(V + 1)]

    for i in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    leaf = 0
    max_dist = 0

    DFS(1)
    DFS(leaf)

    print(max_dist)