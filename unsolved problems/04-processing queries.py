# Sử dụng hàng đợi để xử lí bài toán này.

# Bước 1: Khởi tạo

# Khởi tạo hàng đợi QQ, ta sẽ đẩy truy vấn đầu tiên vào hàng đợi.
# Khởi tạo biến s = t[0]s=t[0], với ý nghĩa s là thời điểm mà ta đang xét đến.
# Mảng lưu kết quả res[i] = -1res[i]=−1 với 0 <= i <= n
# Bước 2: Lặp khi hàng đợi truy vấn khác rỗng

# Gán i = fronti=front, giá trị đầu trong hàng đợi, đồng thời lấy giá trị đó ra khỏi hàng đợi. Việc này đồng nghĩa với việc ta sẽ cho máy chủ xử lí truy vấn thứ ii.
# Cập nhật kết quả res[i] = s + d[i]res[i]=s+d[i], là thời điểm kết thúc quá trình xử lí truy vấn ii. Cập nhật lại thời gian hiện tại s = res[i]s=res[i].
# Tiêp theo ta tìm những truy vấn jj xuất hiện trong khi máy chủ đang xử lí truy vấn ii, t[j] < st[j]<s. Kiểm tra nếu kích thước hàng đợi nhỏ hơn bb cho trước thì đẩy jj vào hàng đợi.
# Ngoài ra, ta phải xét đến trường hợp nếu hàng đợi truy vấn rỗng và ta không có truy vấn jj nào xuất hiện trước thời điểm ss. Trong trường hợp đó, ta sẽ đẩy truy vấn jj đang xét đến vào hàng đợi và nếu t[j] > st[j]>s thì sẽ cập nhật lại s = t[j]s=t[j].
# Độ phức tạp: O(n)O(n) với nn là số lượng truy vấn cần xử lý.

import queue
n, b = map(int, input().split())
q = queue.Queue()
processing = 0
 
for _ in range(n):
    t, d = map(int, input().split())
 
    while q.qsize() != 0 and t >= q.queue[0]:
        q.get()
 
    if q.qsize() <= b:
        processing = max(t, processing) + d
        q.put(processing)
        print(processing, end=' ')
    else:
        print(-1, end=' ')