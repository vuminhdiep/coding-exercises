# Cách giải đơn thuần là với mỗi thao tác loại 22, ta chỉ cần đi sắp xếp lại mảng chứa danh sách đánh giá hiện tại giảm dần và in ra đánh giá thứ floor(n/3)floor(n/3) (mảng bắt đầu từ 11).

# \rightarrow→ Cách này sẽ bị TLE do mỗi lần sort mảng sẽ tốn nhiều thời gian. Thay vào đó ta sử dụng heap chỉ tốn thời gian khi thêm đánh giá mới.

# Tuy nhiên dùng heap đơn thuần thì chỉ có thể lấy phần tử trên đầu, mà muốn biết đánh giá thứ floor(n/3)floor(n/3) thì phải thực hiện lấy ra ra từng cái, và sau đó phải đưa vào heap lại.

# Ta có một nhận xét khác:

# Khi có một đánh giá có điểm số cao hơn so với đánh giá có số điểm thấp nhất hiện tại trong top thì mới được thêm vào top, còn cái thấp nhất sẽ bị loại khỏi top và nằm trong phần còn lại của danh sách đánh giá.
# Top được tính là floor(n/3)floor(n/3), nên khi số đánh giá ít hơn 33 thì không có đánh giá nào trong top, khi bằng 3 \le n \le 53≤n≤5 có 1 đánh giá trong top, 6 \le n \le 86≤n≤8 có 2 đánh giá trong top, cứ tiếp tục như vậy. Nói cách khác khi số đánh giá tăng đến khi chia hết cho 33 thì số đánh giá trong top tăng lên 11.
# Vậy ta sẽ sử dụng 2 hàng đợi ưu tiên:

# Min-heap để lưu top 33 đánh giá tích cực – top của min-heap là đánh giá có số điểm nhỏ nhất hiện tại.
# Max-heap lưu phần còn lại.
# Khi có một đánh giá mới có số điểm xx, ta so sánh nếu xx lớn hơn top của min-heap thì đem top đó bỏ qua max-heap và đẩy xx vào min-heap. Ngược lại, đẩy xx vào max-heap. Sau đó, nếu số đánh giá hiện tại chia hết cho 33 thì lấy top của max-heap đem qua min-heap để tăng số trong top lên 11. Đánh giá hiện tại có điểm nhỏ nhất trên web là top của min-heap.

# Độ phức tạp: O(NlogN)O(NlogN) với NN là số lượng thao tác.

import heapq
top3 = []
rest = []
nreviews = 0

n = int(input())

for _ in range(n):
    line = list(map(int, input().split()))
    type = line[0]
    
    if type == 1:
        x = line[1]
        nreviews += 1

        if len(top3) != 0 and top3[0] < x:
            heapq.heappush(rest, -heapq.heappop(top3))
            heapq.heappush(top3, x)
        else:
            heapq.heappush(rest, -x)

        if nreviews % 3 == 0:
            heapq.heappush(top3, -heapq.heappop(rest))
    else:
        if len(top3) == 0:
            print("No reviews yet")
        else:
            print(top3[0])