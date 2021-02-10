# Sử dụng DSU, khi gặp các cạnh thì ta thực hiện gộp hai tập hợp chứa hai đỉnh của cạnh lại với nhau thành một thành phần liên thông lớn. Đến cuối thì ta duyệt qua danh sách đỉnh, nếu đỉnh nào có parentparent là chính nó (hoặc -1, tùy giá trị khởi tạo) thì nghĩa là đây là đỉnh đại diện của một tập hợp mới (một thành phần liên thông cực đại). Vậy kết quả của ta chính là số lượng đỉnh như vậy.
#
# Độ phức tạp O(T*N*M)O(T∗N∗M) trong trường hợp sử dụng DSU cơ bản, nếu sử dụng DSU nâng cao (update by rank, path compression, by size) thì sẽ là O(T*M*logN)O(T∗M∗logN) với TT là số bộ test, NN là số đỉnh của đồ thị và MM là số cạnh tối đa của đồ thị.

import sys

def getroot(lab, u):
    if lab[u] == -1:
        return u
    lab[u] = getroot(lab, lab[u])
    return lab[u]

def union(lab, cou, a, b):
    if cou[a] > cou[b]:
        cou[a] += cou[b]
        lab[b] = a
    else:
        cou[b] += cou[a]
        lab[a] = b

def convert_number(x):
    return ord(x) - ord('A')

def solve():
    inf = sys.stdin
    input = []
    for line in inf:
        input.append(line)
    len_input = len(input)
    k = 0
    testcase = int(input[k])
    k+=1
    for t in range(testcase):
        k+=1
        x = list(input[k])[0]
        k+=1
        n = convert_number(x) + 1
        lab = [-1 for i in range(n)]
        cou = [1 for i in range(n)]
        while k < len_input and input[k] != '\n':
            temp = list(input[k])
            u = convert_number(temp[0])
            v = convert_number(temp[1])
            k+=1
            u = getroot(lab, u)
            v = getroot(lab, v)
            if u != v:
                union(lab, cou, u, v)
        ans = lab.count(-1)
        if t == testcase - 1:
            print(ans)
        else:
            print("{}\n".format(ans))

solve()