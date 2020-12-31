# Bạn sẽ tính khoảng cách của tất cả các cặp tòa nhà, trừ những tòa nhà nào đã có kết nối rồi thì bạn đặt chi phí kết nối là 00.
#
# Sau khi đã tính xong thì bạn bỏ toàn bộ các cặp kết nối và chi phí đó vào graph rồi chạy thuật toán Prim.
#
# Cây khung nhỏ nhất là kết quả tìm được.
#
# Độ phức tạp: O(T * N^2 * logN)O(T∗N
# ​2
# ​​ ∗logN) với TT là số lượng bộ test và O(N^2 * logN)O(N
# ​2
# ​​ ∗logN) là độ phức tạp của thuật toán Prim vì trong bài này ta dùng tất cả cạnh nối giữa các tòa nhà nên số lượng cạnh là N^2N
# ​2
# ​​ .


import queue
import math


class Scanner:
    def __generator__():
        while True:
            try:
                buff = input().strip().split()
                for x in buff:
                    yield x
            except EOFError:
                exit()

    sc = __generator__()

    def next():
        return Scanner.sc.__next__()


class node:
    dist = 0
    index = 0

    def __init__(self, dist, index):
        self.dist = dist
        self.index = index

    def __lt__(self, other):
        return self.dist < other.dist


def prim(graph, src):
    # graph = matrix [n][n]
    n = len(graph)
    dist = [1e9] * n
    visited = [0] * n
    total_cost = 0
    dist[src] = 0
    Q = queue.PriorityQueue()
    Q.put(node(0, src))

    while not Q.empty():
        temp = Q.get()
        u = temp.index
        visited[u] = True
        for v in range(n):
            if not visited[v] and dist[v] > graph[u][v]:
                dist[v] = graph[u][v]
                Q.put(node(dist[v], v))

    for i in range(n):
        total_cost += dist[i]
    return total_cost


def distance(x1, y1, x2, y2):
    square_dis = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return math.sqrt(square_dis)


def solve():
    while True:
        n = int(Scanner.next())
        x = [0] * n
        y = [0] * n
        for i in range(n):
            x[i], y[i] = int(Scanner.next()), int(Scanner.next())
        graph = []
        for i in range(n):
            graph.append([])
            for j in range(n):
                graph[i].append(distance(x[i], y[i], x[j], y[j]))
        m = int(Scanner.next())
        for i in range(m):
            u, v = int(Scanner.next()), int(Scanner.next())
            u -= 1
            v -= 1
            graph[u][v] = 0
            graph[v][u] = 0
        print("%.2f" % prim(graph, 0))


solve()
