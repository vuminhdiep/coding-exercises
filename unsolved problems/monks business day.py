# Thực chất bài toán yêu cầu chúng ta tìm xem có tồn tại một chu trình dương nào không.
#
# Với thuật toán Bellman-Ford dùng để xác định sự tồn tại của chu trình âm, ta chỉ cần đổi dấu của trọng số là có thể xác định được chu trình dương.

INF = 10 ** 9


def BellmanFord(s):
    dist = [INF] * (n + 1)
    dist[s] = 0

    for i in range(n):
        for edge in graph:
            u, v, w = edge

            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

                if i == n - 1:
                    return True

    return False


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    graph = []

    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, -w))

    print("Yes" if BellmanFord(1) else "No")