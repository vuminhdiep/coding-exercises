# https://codeforces.com/problemset/problem/518/A

# Chạy ngược chuỗi SS từ ký tự cuối về ký tự đầu, xét hai trường hợp sau:
# Nếu gặp ký tự ‘z’ thì biến ký tự này thành ký tự ‘a’.
# Nếu gặp ký tự khác ‘z’ thì tăng ký tự này lên một bậc,
# nghĩa là nếu gặp ký tự ‘b’ thì biến thành ‘c’, ký tự là ‘g’ thì biến thành ‘h’. Ngay sau tăng ký tự lên một bậc thì dừng vòng lặp.
# Sau khi biến đổi xong hãy so sánh giữa chuỗi kết quả và TT, nếu chuỗi kết quả khác chuỗi TT
# (nghĩa là chuỗi nhỏ hơn TT) thì in ra chuỗi kết quả, ngược lại in “No such string”.

s = list(input())
t = list(input())

for i in range(len(s) - 1, -1, -1):
    if s[i] == 'z':
        s[i] = 'a'
    else:
        s[i] = chr(ord(s[i]) + 1)
        break

print(''.join(s) if s != t else "No such string")