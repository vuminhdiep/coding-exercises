# Ta thấy rằng hình ảnh Cthulhu thực chất một đồ thị liên thông và có đúng một chu trình, vậy thì nếu ta bỏ một cạnh trong chu trình ra thì phần còn lại sẽ tạo thành một cây khung của đồ thị. Như vậy, ta suy ra điều kiện đề đồ thị đã cho là Cthulhu: - Đồ thị có số cạnh bằng số đỉnh (vì đồ thị NN đỉnh sẽ có cây khung N – 1 cạnh, thêm 1 cạnh dư tạo thành chu trình nữa thì đồ thị đó sẽ phải có đúng NN cạnh). - Đồ thị này liên thông với nhau. Như vậy, ta chỉ cần kiểm tra xem NN có bằng MM hay không, nếu thỏa, đọc vào các cạnh và sử dụng DSU để gom các tập đỉnh lại với nhau, lúc này kiểm tra nếu đồ thị liên thông (tức NN đỉnh chỉ thuộc một tập duy nhất) thì có thể kết luận đây là Cthulhu. Lưu ý rằng đề bài có yêu cầu số đỉnh tối thiểu phải là 3. Nhưng vì đồ thị nếu có 1 hoặc 2 đỉnh thì sẽ không thể tạo thành chu trình (vì đồ thị không có cạnh song song hoặc tự vòng), nên ta sẽ không cần phải kiểm tra điều kiện này.
#
# Độ phức tạp: O(N*M)O(N∗M) trong trường hợp sử dụng DSU cơ bản, nếu sử dụng DSU nâng cao (update by rank, path compression, by size) thì sẽ là O(M*logN)O(M∗logN) với NN là số đỉnh và MM là số cạnh.


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

def inp():
    return map(int, input().split())

def solve():
    n, m = inp()
    lab = [-1 for i in range(n)]
    cou = [1 for i in range(n)]

    if n != m:
        print("NO") #impossible
        return

    for i in range(m):
        u, v = inp()
        u = getroot(lab, u-1)
        v = getroot(lab, v-1)
        if u != v:
            union(lab, cou, u, v)
    if lab.count(-1) > 1: #not connected
        print("NO")
        return

    print("FHTAGN!")

solve()