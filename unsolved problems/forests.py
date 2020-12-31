# Ta có thể sử dụng DSU để giải bài này như sau:
#
# Với mỗi người, ta sử dụng một mảng lưu những cây mà họ nghĩ đã gây ra tiếng ngã.
# Sau khi đọc xong dữ liệu, ta tiến hành thực hiện thao tác union với những cặp người nào có các phần tử trong mảng lưu giống nhau toàn bộ.
# Cuối cùng in ra số lượng tập hợp được tạo thành. Biết rằng một đỉnh mà có đỉnh cha bằng với chính nó được xem là một phần tử đại diện của tập hợp.
# Độ phức tạp: O(Q * P^2 * (T + P))O(Q∗P
# ​2
# ​​ ∗(T+P)) cho DSU cơ bản hoặc O(Q * P^2 * (T + log(P)))O(Q∗P
# ​2
# ​​ ∗(T+log(P))) cho DSU nâng cao với QQ, PP, TT lần lượt là số trường hợp, số người và số cây trong mỗi trường hợp.


def findSet(u):
    if u != parent[u]:
        parent[u] = findSet(parent[u])
    return parent[u]


def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)

    if up == vp:
        return

    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1


Q = int(input())
input()

while Q > 0:
    P, T = map(int, input().split())
    trees = [set() for i in range(P + 1)]
    parent = [i for i in range(P + 1)]
    ranks = [0 for i in range(P + 1)]

    while True:
        try:
            line = input()
            if not line:
                break
            person, tree = map(int, line.split())
            trees[person].add(tree)
        except EOFError:
            break

    for i in range(1, P + 1):
        for j in range(i + 1, P + 1):
            if trees[i] == trees[j]:
                unionSet(i, j)

    nSets = sum(1 for i in range(1, P + 1) if i == parent[i])
    print(nSets)
    Q -= 1

    if Q > 0:
        print()