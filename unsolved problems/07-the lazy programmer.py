# Ta có nhận xét sau: nếu trả thêm xx dollars thì công việc thứ ii sẽ được hoàn thành trong khoảng thời gian là b_i - a_i * xb
# ​i
# ​​ −a
# ​i
# ​​ ∗x, nói cách khác là công việc sẽ rút ngắn được a_i * xa
# ​i
# ​​ ∗x đơn vị thời gian. Vậy ta ưu tiên chọn công việc có a_ia
# ​i
# ​​  lớn hơn, vì với cùng một khoản xx dollars bỏ ra, a_ia
# ​i
# ​​  nào càng lớn thì thời gian rút ngắn được càng nhiều.

# Giải quyết bài này, ta sẽ thực hiện các bước sau:

# Bước 1: Chuẩn bị

# Sắp xếp lại các hợp đồng theo deadline d_id
# ​i
# ​​  tăng dần để đảm bảo deadline d_id
# ​i
# ​​  nào tới sớm hơn thì phải được thực hiện trước.
# Tạo một priority queue, gọi là pqpq để lưu thông tin hợp đồng ii, ưu tiên theo aa. Nói cách khác là xây dựng một heap-max ưu tiên theo aa.
# Khởi tạo time = 0time=0, summin = 0summin=0 (với timetime dùng để lưu tổng các b_ib
# ​i
# ​​ , summinsummin dùng để lưu tổng các khoản trả thêm bé nhất có thế).
# Bước 2: Xử lí, duyệt qua các hợp đồng ii

# Cộng dồn b_ib
# ​i
# ​​  vào timetime và thêm thông tin của hợp đồng ii vào priority queue pqpq.
# Trong khi time > d_itime>d
# ​i
# ​​ , tức là ta cần hạ timetime xuống dần sao cho timetime đúng bằng d_id
# ​i
# ​​  để hoàn thành hợp đồng ii đúng thời hạn: Gọi toptop là phần tử đầu tiên của pqpq. Pop phần tử này ra khỏi pqpq.
# Nếu (top.b(top.b >> timetime – d_i)d
# ​i
# ​​ ), ta sẽ chọn (time(time – d_i)d
# ​i
# ​​ ) để số tiền xx cần chi ra thấp hơn.
# Cộng thêm một khoản xx == (time(time – d_i)/top.ad
# ​i
# ​​ )/top.a.
# Giảm top.btop.b đi một lượng thời gian là (time(time – d_i)d
# ​i
# ​​ ).
# Bỏ toptop lại vào pqpq.
# Gán lại time = d_itime=d
# ​i
# ​​ .
# Ngược lại: nếu (top.b(top.b \le≤ timetime – d_i)d
# ​i
# ​​ ), ta sẽ chọn top.btop.b để số tiền xx cần bỏ ra thấp hơn.
# Cộng thêm một khoản xx == top.b/top.atop.b/top.a vào summinsummin.
# Hạ timetime xuống một lượng là top.btop.b.
# Gán top.btop.b == 00.
# Bước 3: Xuất kết quả, in summinsummin làm tròn hai chữ số phần thập phân. Khởi tạo lại time = 0time=0, summin = 0summin=0 và khởi tạo lại pqpq rỗng để chuẩn bị cho testcase kế tiếp.

# Độ phức tạp: O(t*NlogN)O(t∗NlogN) với tt là số lượng testcases và NN là số lượng hợp đồng ứng với mỗi testcase.

import queue
def solve():
    n = int(input())
    jobs = []
    for i in range(n):
        a, b, d = map(int, input().split())
        jobs.append((d, a, b))
    
    jobs.sort()
    pq = queue.PriorityQueue()
    time = 0
    money = 0
    for d, a, b in jobs:
        time += b
        pq.put((-a, b, d))
        while time > d:
            ta, tb, td = pq.get()
            if tb > time - d:
                tb -= time - d
                money += (time - d) / -ta
                time = d
                pq.put((ta, tb, td))
            else:
                time -= tb
                money += tb / -ta

    print('{:.2f}'.format(money))

T = int(input())
for t in range(T):
    solve()