# Rõ ràng nếu như ta xem như mỗi người là một đỉnh trên một đồ thị, thì việc đánh số cho một người có số là 0, sau đó ta đi đánh số đến những người bạn của người đó, thì rõ ràng ta có thể thấy ý tưởng thuật toán BFS lộ rõ ra ngay từ suy nghĩ này. Như vậy, ý tưởng của ta là ta sẽ quy định những người này là một đỉnh của đồ thị, sau đó sử dụng BFS để loang ra đánh số đỉnh tương ứng. Để có thể ánh xạ được từ một chuỗi sang một con số để có thể đánh số được đỉnh của đồ thị, ta sử dụng một cây nhị phân tìm kiếm key-value với key là string (tên mỗi người) và value là một con số ánh xạ tương ứng. Khi ta nhập một chuỗi ss, nếu người có tên là ss chưa được đánh số đồ thị (chưa xuất hiện trước đây) thì ta tiến hành đánh số đỉnh cho người đó.
#
# Độ phức tạp: O(NlogN + N + M), với việc ánh xạ từng tên sang số thì ta có độ phức tạp là O(NlogN)O(NlogN) cho việc ánh xạ toàn bộ. Ngoài ra, thuật toán duyệt BFS của ta có độ phức tạp là O(N+M)O(N+M) với NN là số lượng đỉnh và MM là số lượng cạnh.
#

import queue


def BFS(graph, src, rank):
    Q = queue.Queue()
    rank[src] = 0
    Q.put(src)
    while not Q.empty():
        u = Q.get()
        for v in graph[u]:
            if rank[v] == 'undefined':
                rank[v] = rank[u] + 1
                Q.put(v)
    return rank


def solve():
    n = int(input())
    S = dict()
    cnt = 0
    graph = []
    for i in range(n):
        line = input().split()
        v = []
        for name in line:
            if name in S:
                id = S[name]
            else:
                S[name] = cnt
                id = cnt
                graph.append([])
                cnt += 1
            v.append(id)
        for x in v:
            for y in v:
                if x != y:
                    graph[x].append(y)
    rank = ['undefined' for i in range(cnt)]
    if 'Isenbaev' in S:
        rank = BFS(graph, S['Isenbaev'], rank)
    a = []
    for name in S:
        a.append(name)
    a.sort()
    for name in a:
        print(name + ' ' + str(rank[S[name]]))


solve()
