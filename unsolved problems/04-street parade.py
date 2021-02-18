# Nhận xét:

# Ta có thể mô phỏng hoạt động của con hẻm bằng CTDL stack với nguyên lý xe nào vào hẻm sau thì có thể đi ra trước.
# Các chiếc xe được trình diễn theo số thứ tự từ nhỏ đến lớn, tức từ xe có số thứ tự 1 đến số thứ tự n. Do đó, ta hoàn toàn có thể biết được chiếc xe hiện tại đang cần đưa ra trình diễn có số thứ tự là bao nhiêu bằng cách sử dụng một biến đếm.
# Như vậy, với mỗi lần cần đưa một chiếc xe ra trình diễn, ta đối chiếu số thứ tự của xe được yêu cầu với xe ở bãi đỗ và xe ở hẻm để quyết định đưa xe nào ra trình diễn. Trong trường hợp không có xe nào được đem ra, ta cần đưa xe đang đỗ trong bãi vào hẻm để xét xe kế tiếp nằm trong bãi.
# Ta có các bước giải bài này như sau:

# Bước 1: Đọc thông tin các xe hiện có trong bãi vào một mảng.
# Bước 2: Khởi tạo một stack dùng để mô phỏng con hẻm. Ban đầu stack rỗng.
# Bước 3: Sử dụng một biến đếm lưu số thứ tự xe cần để đem ra trình diễn với giá trị khởi tạo bằng 1.
# Bước 4: Duyệt qua từng chiếc xe trong bãi:
# Nếu số thứ tự đang cần đúng bằng số thứ tự xe trong bãi đỗ xe thì đưa xe này ra trình diễn và tăng thứ tự trình diễn.
# Ngược lại, xét xem xe trong hẻm có phù hợp không:
# Nếu có, đem xe trong hẻm ra trình diễn và tăng thứ tự trình diễn.
# Nếu không, nghĩa là cả xe đang nằm trong bãi và xe đầu hẻm đều không đúng thứ tự, ta đưa xe hiện tại trong bãi vào hẻm để xét xe kế tiếp.
# Bước 5: Nếu hết xe trong bãi đỗ, ta cần kiểm tra các xe còn lại trong hẻm có thỏa thứ tự còn lại hay không và đưa ra trình diễn nếu đúng.
# Bước 6: Kiểm tra biến lưu thứ tự trình diễn. Nếu biến đạt tới thứ tự (N + 1) nghĩa là ta đã đem đủ n chiếc xe ra trình diễn, in “yes”. Ngược lại, in “no”.
# Bước 7: Reset các biến cần thiết, chuẩn bị cho bộ test tiếp theo.

while True:
    n = int(input())
    if n == 0:
        break
    trucks = list(map(int, input().split()))
    side_trucks = []
    ordering = 1
    i = 0
 
    while i < n:
        if trucks[i] == ordering:
            ordering += 1
            i += 1
        elif side_trucks and side_trucks[-1] == ordering:
            ordering += 1
            side_trucks.pop()
        else:
            side_trucks.append(trucks[i])
            i += 1
     
    while side_trucks and side_trucks[-1] == ordering:
        ordering += 1
        side_trucks.pop()
 
    print('yes' if ordering == n + 1 else 'no')