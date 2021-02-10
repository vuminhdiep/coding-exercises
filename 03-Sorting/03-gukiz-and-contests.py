# https://codeforces.com/problemset/problem/551/A

# Nhận xét:
#
# Ta thấy rằng vì những người có cùng điểm số sẽ cùng hạng, do đó tương ứng với mỗi giá trị điểm số, ta sẽ chỉ có một giá trị thứ hạng cố định.
# Để nhanh chóng truy xuất được thứ hạng của một học sinh, hay nói cách khác là trả lời cho câu hỏi với điểm số như vậy thì học sinh đó sẽ được hạng bao nhiêu, ta lập bằng lưu thứ hạng theo điểm số.
# Nếu sắp điểm số theo thứ tự từ cao đến thấp, thì thứ hạng của một điểm số chính bằng vị trí mà điểm số đó xuất hiện lần đầu tiên (vị trí tính từ 11).
# Ta có cách giải của bài này như sau:
#
# Bước 1: Đưa thông tin điểm số vào một mảng - mảng này sẽ là mảng gốc mà ta sẽ duyệt lại cuối cùng để đưa ra kết quả.
# Bước 2: Sao chép thông tin điểm số trong mảng gốc vào một mảng mới và sắp xếp theo thứ tự từ cao đến thấp.
# Bước 3: Khởi tạo mảng lưu thứ hạng theo điểm số với giá trị mặc định bằng 00.
# Bước 4: Sử dụng vòng lặp ii duyệt qua điểm số đã được sắp xếp trên:
# Nếu thứ hạng của điểm số hiện tại chưa được ghi nhận (tức thứ hạng bằng 00):
# Cập nhật thứ hạng của điểm số đó bằng (1 + i)(1+i).
# Ngược lại, không làm gì.
# Bước 5: Duyệt lại mảng gốc ban đầu, in ra thứ hạng theo điểm số tương ứng.
# Độ phức tạp: O(nlogn)O(nlogn) với nn là số lượng sinh viên tham gia kiểm tra.

n = int(input())
ratings = list(map(int, input().split()))
sorted_ratings = sorted(ratings, reverse=True)
ranked = [0] * 2005

for i in range(n):
    rating = sorted_ratings[i]
    if not ranked[rating]:
        ranked[rating] = i + 1

for rating in ratings:
    print(ranked[rating], end=' ')


#Cach 2

n =int(input())
l = list(map(int,input().split()))
t=sorted(l,reverse=True)
for i in l:
    print(t.index(i)+1) #returns the position at the first occurrence of the specified value.