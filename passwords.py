# Passwords
# https://codeforces.com/problemset/problem/721/B

# Theo cách nhập mật khẩu của Vanya, các mật khẩu có chiều dài nhỏ nhất sẽ được nhập trước,
# rồi đến các mật khẩu có chiều dài nhỏ thứ hai, cứ tiếp tục như vậy. Đến khi chiều dài bằng chiều dài mật khẩu đúng,
# thì trường hợp tốt sẽ nhập đúng ngay lần đầu tiên, trường hợp xấu sẽ nhập đúng sau khi đã nhập tất cả mật khẩu cùng chiều dài.
# Vậy với nn mật khẩu, ta sẽ đếm xem ứng với mỗi chiều dài thì có bao nhiêu chuỗi cùng chiều dài đó, lưu lại thông tin này.
# Sau đó, để tìm thời gian cho trường hợp tốt nhất, đi tính tổng số mật khẩu có chiều dài nhỏ hơn chiều dài mật khẩu đúng,
# đây cũng là thời gian dành để nhập các mật khẩu. Sau kk lần nhập sai thì bị chặn 5 giây, nên ta lấy tổng vừa tìm được chia cho kk ra được số lần bị chặn,
# rồi nhân cho 5, ta sẽ biết được tổng số thời gian bị chặn.
# Ta lấy tổng số mật khẩu tìm được trước đó cộng với tổng thời gian bị chặn sẽ biết được tổng thời gian nhập các mật khẩu sai có chiều dài nhỏ hơn chiều dài mật khẩu đúng.
# Thực hiện tương tự để tìm thời gian cho trường hợp xấu nhất, nhưng chỗ tính tổng số mật khẩu, ta cộng thêm số mật khẩu cùng chiều dài với mật khẩu đúng, nhớ trừ đi 1 (trừ mật khẩu đúng).
# Lấy kết quả ở cả hai trường hợp ta đã tính được cộng thêm 1 (thời gian nhập mật khẩu đúng) là ra đáp án cuối cùng.
# Độ phức tạp: O(n + length(s))O(n+length(s)) với nn là số lượng chuỗi nhập và length(s)length(s) là độ dài chuỗi ss là chuỗi mật khẩu đúng.

n, k = map(int, input().split())
password = []
for i in range(n):
    s = input()
    password.append(s)
res = input()
lower, upper = 0, 0

for i in range(n):
    lower += (len(password[i]) < len(res))
    upper += (len(password[i]) <= len(res))

print(lower + (lower // k) * 5 + 1, upper + ((upper - 1) // k) * 5)