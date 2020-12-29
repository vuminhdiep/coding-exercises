# https://codeforces.com/problemset/problem/451/B

# Nhận xét:
#
# Trước hết, ta thấy rằng hoàn toàn có thể biết được mảng kết quả sau khi đã được sắp tăng dần bằng việc áp dụng thuật toán sắp xếp đối với mảng ban đầu.
# Đoạn con mà khi đảo ngược nó, ta thu được mảng tăng dần sẽ bắt đầu từ vị trí đầu tiên mà mảng kết quả khác với mảng ban đầu. Tương tự, đoạn con đó sẽ kết thúc tại vị trí cuối cùng mà mảng kết quả khác với mảng ban đầu.
# Tuy nhiên, việc đảo ngược đoạn con vừa tìm được chưa chắc sẽ cho ta một mảng tăng dần. Do đó, ta cần so sánh mảng sau khi đã đảo ngược đoạn con với mảng kết quả tăng dần để đưa ra đáp án.
# Như vậy, các bước thực hiện của ta như sau:
#
# Bước 1: Đưa các phần tử vào mảng.
# Bước 2: Sắp xếp lại mảng tăng dần, đây chính là mảng kết quả nói trên.
# Bước 3: Chạy song song từ trái sang phải trên hai mảng ban đầu và mảng đã sắp để tìm vị trí đầu tiên sai khác, tạm gọi là ll.
# Bước 4: Làm tương tự từ phải sang trái để tìm vị trí cuối cùng sai khác, tạm gọi là rr.
# Bước 5: Đảo ngược đoạn con [l, r][l,r].
# Bước 6: So sánh mảng sau khi đã đảo ngược đoạn con với mảng kết quả, nếu trùng khớp thì in yes và đoạn [l, r][l,r], ngược lại in no.
# Độ phức tạp: O(nlogn)O(nlogn) với nn là số lượng phần tử trong mảng.


n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)
l = r = 0

for i in range(n):
    if a[i] != sorted_a[i]:
        l = i
        break

for i in range(len(a) - 1, -1, -1):
    if a[i] != sorted_a[i]:
        r = i
        break

i, j = l, r
while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1

if a != sorted_a:
    print('no')
    exit()

print('yes')
print('{} {}'.format(l + 1, r + 1))