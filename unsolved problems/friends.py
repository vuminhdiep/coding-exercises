# Ta có thể sử dụng DSU để giải bài toán này như sau:
#
# Với mỗi cặp bạn bè, ta sử dụng thao tác union để đưa họ vào cùng một nhóm bạn.
# Tuy nhiên, để dễ dàng biết được trong một nhóm bạn có bao nhiêu người, ta sử dụng thêm một mảng đếm số lượng phần tử ứng với phần tử đại diện. Khi hợp tập hợp của uu và vv, ta cộng dồn số lượng phần tử của tập con vào số lượng phần tử của tập được chọn làm cha.
# Cuối cùng in ra số lượng người trong nhóm đông nhất, hay số phần tử trong tập hợp lớn nhất.


def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u


def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if vp != up:
        parent[up] = vp
        cnt[vp] += cnt[up]


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    cnt = [1 for i in range(n + 1)]

    for i in range(m):
        u, v = map(int, input().split())
        unionSet(u, v)

    print(max(cnt))