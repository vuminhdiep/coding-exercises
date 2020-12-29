# https://codeforces.com/problemset/problem/334/B

# Giải thích ví dụ
# Ví dụ 1: Ta thấy các giao điểm được cho đều thuộc giao điểm của 3 đường thẳng ngang x = 0, x = 1 và x = 2 với 3 đường thẳng dọc y = 0, y = 1, y = 2 trừ giao điểm chính giữa là (2, 2). Do đó đây là tập 8 điểm hợp lệ, in “respectable”.
#
# Ví dụ 2: Ta thấy các giao điểm được cho nằm rải rác trên các đường thẳng ngang x = {0..7} với đường thẳng dọc y = 0. Do đó đây không phải là tập 8 điểm hợp lệ, in “ugly”.
#
# Ví dụ 3: Ta thấy các giao điểm được cho đều thuộc giao điểm của 3 đường thẳng ngang x = 1, x = 2 và x = 3 với 3 đường thẳng dọc y = 1, y = 2, y = 3. Tuy nhiên, tập 8 điểm này lại chứa cả giao điểm chính giữa là (2, 2). Do đó đây không phải là tập hợp lệ, in “ugly”.
#
# Hướng dẫn giải
# Nhận xét:
#
# Giả sử đã biết được 3 giá trị phân biệt của x và 3 giá trị phân biệt của y, ta hoàn toàn có thể phát sinh ra tập 8 điểm hợp lệ bằng cách sử dụng hai vòng lặp lồng nhau. Từ đây, ta chỉ việc so sánh với tập 8 điểm của đề bài, nếu giống nhau hoàn toàn thì in “respectable”, ngược lại in “ugly”.
# Sử dụng hai mảng đánh dấu để lấy được các giá trị phân biệt của x và y.
# Nhằm giúp việc so sánh tập 8 điểm do ta phát sinh và tập 8 điểm đề cho được thuận lợi hơn, ta quy định các cặp điểm khi so sánh phải được sắp xếp tăng dần theo thứ tự của x. Nếu x giống nhau thì sắp tăng dần theo y.
# Như vậy, ta có cách giải của bài này như sau:
#
# Bước 1: Đọc vào tập 8 điểm đề cho, với mỗi điểm (x, y) ta thực hiện:
# Đưa (x, y) vào một mảng lớn.
# Kiểm tra giá trị x đã xuất hiện trước đây hay chưa. Nếu chưa, đưa x vào mảng chứa các giá trị phân biệt của x.
# Thực hiện tương tự với y.
# Bước 2: Sau khi đã có được mảng chứa các giá trị x phân biệt và y phân biệt, ta kiểm tra điều kiện có đúng 3 giá trị x phân biệt và 3 giá trị y phân biệt. Nếu vi phạm, ta lập tức kết luận tập 8 điểm đề cho là không hợp lệ và in ra "ugly".
# Bước 3: Sắp xếp mảng các giá trị phân biệt của x và y tăng dần, chuẩn bị cho quá trình phát sinh tập 8 điểm hợp lệ. Đồng thời, sắp xếp mảng chứa tập 8 điểm của đề bài cũng theo thứ tự tăng dần.
# Bước 4: Sử dụng một biến đếm lưu vị trí điểm đang xét trong mảng chứa tập 8 điểm đã được sắp. Bắt đầu phát sinh từng cặp phần tử (xi, yj) bằng hai vòng lặp lồng nhau trên hai mảng chứa các giá trị phân biệt của x và y:
# Nếu i = j = 2, ta bỏ qua không xét vì đây là giao điểm chính giữa.
# Ngược lại, ta kiểm tra liệu điểm đang xét có bằng cặp (xi, yi) theo thứ tự đang được phát sinh không. Nếu đúng, ta di chuyển đến điểm tiếp theo. Ngược lại, ta có thể kết luận tập 8 điểm đề cho là không hợp lệ và in “ugly”.
# Bước 5: Hoàn thành các bước trên, ta chắc chắn tập 8 điểm đề cho hoàn toàn khớp với tập 8 điểm hợp lệ mà ta phát sinh nên in “respectable”.
# Độ phức tạp: O(NlogN)O(NlogN) với N = 8.


fre_x = [False] * (10 ** 6 + 5)
fre_y = [False] * (10 ** 6 + 5)
unique_x = []
unique_y = []
points = []

for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

    if not fre_x[x]:
        fre_x[x] = True
        unique_x.append(x)

    if not fre_y[y]:
        fre_y[y] = True
        unique_y.append(y)

if len(unique_x) != 3 or len(unique_y) != 3:
    print('ugly')
    exit()

unique_x.sort()
unique_y.sort()
points.sort()
index = 0

for i in range(3):
    for j in range(3):
        if i == j == 1:
            continue
        if unique_x[i] == points[index][0] and unique_y[j] == points[index][1]:
            index += 1
        else:
            print('ugly')
            exit()

print('respectable')