# Với bài toán này ta sẽ đưa về một tập hợp để xét và sẽ dùng thuật toán DSU để giải quyết vấn đề này. Với dữ liệu đề bài trong một cuộc đàm phán sẽ có tối đa 10000 người (MAX = 10000MAX=10000), vì vậy ta sẽ quy định trong một tập hợp gồm có 2 khoảng [0, 9999)[0,9999) và [10000, 19999)[10000,19999) nếu cả 2 người cần xét cùng nằm trên 1 khoảng thì sẽ là bạn ngược lại là kẻ thù. Khi đó:
#
# Với hoạt động 1: Đầu tiên sẽ phải kiểm tra xx và y + MAXy+MAXcó cùng nằm trong tập hợp hiện tại hay không?
# Nếu có thì in ra -1 và bỏ qua hoạt động setFriendssetFriends vì họ chắc chắn đã là kẻ thù.
# Nếu không, thì ta sẽ gom xx, yy vào cùng nhóm tương tự gom x + MAXx+MAX và y + MAXy+MAX vào cùng nhóm.
# Với hoạt động 2: Đầu tiên sẽ phải kiểm tra xx và yy có cùng nằm trong tập hợp hiện tại hay không?
# Nếu có thì in ra -1−1 và bỏ qua hoạt động setEnemiessetEnemies vì họ chắc chắn đã là bạn.
# Nếu không, thì ta sẽ gom xx và y + MAXy+MAX vào cùng nhóm, tương tự gom x + MAXx+MAX và yy vào cùng nhóm.
# Với hoạt động 3: Nếu xx và yy thuộc cùng 1 nhóm thì in 1 ngược lại in 0.
# Với hoạt động 4: Nếu xx và y + MAXy+MAX thuộc cùng 1 nhóm thì in 1 ngược lại in 0.
# Độ phức tạp: O(n * m)O(n∗m) với nn là số lượng người tham gia và mm là số lượng operations.


import sys
sys.setrecursionlimit(100000)
MAX = 10000

def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[vp] = up

n = int(input())
parent = [i for i in range(MAX * 2)]
while True:
    c, x, y = map(int, input().split())
    if c == x == y == 0:
        break
    if c == 1:
        if findSet(x) == findSet(y + MAX):
            print(-1)
            continue
        unionSet(x, y)
        unionSet(x + MAX, y + MAX)
    if c == 2:
        if findSet(x) == findSet(y):
            print(-1)
            continue
        unionSet(x, y + MAX)
        unionSet(x + MAX, y)
    if c == 3:
        if findSet(x) == findSet(y):
            print(1)
        else:
            print(0)
    if c == 4:
        if findSet(x) == findSet(y + MAX):
            print(1)
        else:
            print(0)