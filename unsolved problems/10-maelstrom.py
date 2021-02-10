# Nhận xét: Nhiệm vụ của ta là tìm thời gian nhỏ nhất đi từ đỉnh 11 đến tất cả các đỉnh còn lại trên đồ thị. Ta dùng Bellman-Ford trên đồ thị có trọng số không âm.
#
# Trước tiên từ nửa dưới của ma trận kề đề cho, ta có thể chuyển sang danh sách cạnh và áp dụng thuật toán Bellman-Ford trên đó.
#
# Cuối cùng lấy thời gian lớn nhất trong các thời gian nhỏ nhất đi từ đỉnh 11 đến một đỉnh ii bất kỳ trong đồ thị. Đây cũng chính là kết quả của bài toán.

def BellmanFord(s, n, dist, graph):
    dist[s] = 0

    for i in range(n - 1):
        for edge in graph:
            u, v, w = edge
            dist[v] = min(dist[v], dist[u] + w)


n = int(input())
dist = [10 ** 9] * (n + 1)
graph = []

for i in range(2, n + 1):
    line = input().split()

    for j in range(1, i):
        if line[j - 1] != 'x':
            w = int(line[j - 1])
            graph.append((i, j, w))
            graph.append((j, i, w))

BellmanFord(1, n, dist, graph)

res = 0
for i in range(1, n + 1):
    res = max(res, dist[i])
print(res)