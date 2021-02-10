# Ý tưởng: Ban đầu cho mỗi số nguyên thuộc 1 tập hợp riêng. Nếu như 1 số nguyên xx đủ điều kiện để vào tập hợp AA thì ta sẽ cho cả xx và a-xa−x vào tập hợp AA. Ta làm điều tương tự với 1 số nguyên đủ điều kiện vào tập hợp BB.
#
# Chuẩn bị: một map lấy tên là mpmp để lưu lại vị trí thứ ii số nguyên p_ip
# ​i
# ​​ , một mảng tên pp để lưu nn số nguyên p_ip
# ​i
# ​​ , một mảng tên fafa để lưu lại cha của p_ip
# ​i
# ​​ . Định nghĩa hai hàm Union và Find để liên kết và tìm đỉnh gốc trong Disjoint Set.
#
# Thực hiện:
#
# Đọc vào n, a, bn,a,b.
# Lần lượt đọc vào các số nguyên p_ip
# ​i
# ​​ , lưu lại vị trí ii của số nguyên ấy với key là p_ip
# ​i
# ​​ , value là ii. Trong quá trình đọc lưu lại giá trị p_ip
# ​i
# ​​  lớn nhất vào 1 biến tên là MaxMax.
# Nếu MaxMax \ge≥ max(a, b)max(a,b) thì ta in ra “NO” và kết thúc chương trình vì khi x = Maxx=Max, a-x \le 0a−x≤0 và b-x \le 0b−x≤0. Vì các số đề cho đều là số dương nên ta không thể đáp ứng điều kiện được. Còn nếu Max < max(a, b)Max<max(a,b) thì ta thực hiện các bước tiếp theo.
# Cho một vòng lặp với biến ii đi từ 00 đến n+1n+1, khởi tạo cho giá trị fa[i]fa[i] bằng ii. Các vị trí trong mảng fafa từ 11 đến nn sẽ lưu vị trí của cha ii. Hai vị trí 00 và n+1n+1 tượng trưng cho 2 tập hợp AA và BB. Bất cứ số nào không đủ điều kiện trong tập hợp AA sẽ được cho vào tập hợp BB và ngược lại. Vì vậy, nếu có bất kì số nào thuộc cả 2 tập hợp (tức là không thoả điều kiện để vào tập hợp nào) thì ta biết là không thể nào thoả điều kiện đề cho và in ra “NO”.
# Sau khi khởi tạo giá trị của fafa, ta sẽ bắt đầu đi vào việc liên kết các phần tử với nhau. Cho một vòng lặp với biến ii đi từ 11 đến nn. Nếu mp[a-p[i]]mp[a−p[i]] tồn tại (tức là số tại giá trị ii đủ đk để tập hợp AA) thì ta dùng hàm Union liên kết hai hai số tại hai vị trí ii và mp[a-p[i]]mp[a−p[i]]. Nếu mp[a-p[i]]mp[a−p[i]] không tồn tại thì ta dùng hàm Union đối với ii và n+1n+1 (tức là ta thêm ii vào tập hợp B).
# Tiếp đến ta kiểm tra nếu mp[b-p[i]]mp[b−p[i]] tồn tại (tức là số tại giá trị ii đủ đk để tập hợp BB) thì ta dùng hàm Union liên kết hai hai số tại hai vị trí ii và mp[b-p[i]]mp[b−p[i]]. Nếu mp[b-p[i]]mp[b−p[i]] không tồn tại thì ta dùng hàm Union đối với ii và 00 (tức là ta thêm ii vào tập hợp AA). Nếu có một giá trị nào không đủ điều kiện để vào cả hai tập hợp A, B thì các thao tác trên sẽ liên kết cả hai tập hợp AA và BB vào cùng 1 tập hợp. Khi ấy thì Find(0)Find(0) sẽ bằng với Find(n+1)Find(n+1).
# Khởi tạo 2 biến AA và BB bằng hai giá trị Find(0)Find(0) và Find(N+1)Find(N+1). Nếu A = BA=B thì ta in ra “NO” và kết thúc chương trình. Ngược lại thì ta sẽ in ra “YES” và in ra rằng các số ban đầu sẽ thuộc tập hợp nào. Cho một vòng lặp với biến ii đi từ 11 tới nn. Nếu như Find(i) = AFind(i)=A (đồng nghĩa với số thứ ii thuộc tập hợp AA) thì ta in ra 00. Nếu như ngược lại thì ta in ra 11.
# LƯU Ý: Nếu số tại vị trí ii đủ điều kiện để thuộc cả hai tập hợp AA và BB thì Find(i)Find(i) sẽ trả ra một giá trị khác với giá trị của cả AA và BB. Tuy nhiên, với điều kiện Find(i) = AFind(i)=A thì những số đủ điều kiện thuộc hai tập hợp AA và BB thì sẽ được tự động xếp vào tập hợp BB.
#
# Độ phức tạp: n*log(n)n∗log(n) với nn là kích thước của dãy số đề cho.




def find(u):
    global par
    if u != par[u]:
        par[u] = find(par[u])
    return par[u]

def union(u, v):
    u = find(u)
    v = find(v)
    par[u] = v

n, a, b = map(int, input().split())
p = list(map(int, input().split()))
mp = dict()
for i in range(n):
    mp[p[i]] = i + 1
par = [i for i in range(n + 2)]

for i in range(n):
    union(i + 1, mp.get(a - p[i], n + 1))
    union(i + 1, mp.get(b - p[i], 0))

A = find(0)
B = find(n + 1)

if A != B:
    print('YES')
    print(' '.join(['1' if find(i) == B else '0' for i in range(1, n + 1)]))
else:
    print('NO')	