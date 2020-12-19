# https://codeforces.com/problemset/problem/6/C

# Sử dụng kỹ thuật Two Pointers với hai biến chạy ii và jj tương ứng với vị trí mà Alice và Bob đang ăn. Đồng thời dùng thêm hai biến lưu thời điểm ăn của cả hai.
#
# Bước 1: Đưa thông tin về thời gian ăn các thanh chocolate vào một mảng.
# Bước 2: Khởi tạo thời điểm ăn của cả hai là 0.
# Bước 3: Sử dụng hai biến chạy ii đầu mảng (Alice) và jj cuối mảng (Bob).
# So sánh thời điểm ăn của Alice và Bob:
# Nếu thời điểm Alice bắt đầu ăn thanh chocolate tại vị trí ii nhỏ hơn hoặc bằng thời điểm Bob ăn thanh chocolate thứ jj thì Alice sẽ ăn thanh chocolate tại vị trí ii.
# Ngược lại Bob sẽ ăn thanh chocolate tại vị trí jj.
# Cập nhật thời điểm ăn của từng người và hai biến chạy ii, jj.
# Bước 4: Số thanh chocolate mà Alice đã ăn được chính bằng giá trị của ii và của Bob là (n - i)(n−i).
# Độ phức tạp O(n)O(n) với nn là số lượng thanh chocolate.

n = int(input())
chocolate = list(map(int, input().split()))
t_alice = t_bob = 0
i, j = 0, n - 1

while i <= j:
    if t_alice + chocolate[i] <= t_bob + chocolate[j]:
        t_alice += chocolate[i]
        i += 1
    else:
        t_bob += chocolate[j]
        j -= 1

print(i, n - i)