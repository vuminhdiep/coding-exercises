# https://codeforces.com/problemset/problem/149/A
#
# Nhận xét:
#
# Ta thấy rằng để cây nhanh chóng đạt chiều cao cần thiết, ta sẽ ưu tiên tưới nước vào những tháng mà cây phát triển mạnh mẽ nhất.
# Do đó, ta hình thành cách giải như sau:
#
# Bước 1: Đưa thông tin độ tăng chiều cao của cây ở mỗi tháng vào một mảng.
# Bước 2: Sắp xếp mảng giảm dần, tháng nào cây phát triển mạnh hơn sẽ đứng trước.
# Bước 3: Sử dụng một biến đếm số lượng tháng cần phải tưới nước và lần lượt duyệt qua mảng đã sắp: Nếu chiều cao cần tăng k vẫn còn lớn hơn 0, tức cây vẫn cần phải phát triển tiếp, ta tăng biến đếm số lượng tháng cần tưới lên 1. Đồng thời trừ độ cao cây phát triển được vào k chiều cao cần phát triển.
# Bước 4: In ra kết quả. Nếu lúc này mà k > 0 tức là đã tưới nước hết 12 tháng mà cây vẫn không đạt yêu cầu, ta in -1. Ngược lại, in ra số tháng đã lưu.
# Độ phức tạp: O(NlogN)O(NlogN) với N = 12 là số lượng tháng.

k = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
n_months = 0

for height in a:
    if k <= 0:
        break

    n_months += 1
    k -= height

print(n_months if k <= 0 else -1)