# Bài này ta chỉ việc đi mô phỏng lại các thao tác ứng với ba cấu trúc được đề cập và kiểm tra.

# Đầu tiên, chuẩn bị 33 biến đánh dấu CTDL có thể thuộc 33 loại stackstack, queuequeue hay prioritypriority queuequeue. Ban đầu chưa biết CTDL đó là gì thì ta mặc định 33 biến này đều có giá trị 11 (truetrue). Đồng thời khởi tạo 33 CTDL stackstack, queuequeue và prioritypriority queuequeue.

# Với lệnh type = 1type=1, ta đẩy xx vào stackstack, queuequeue và prioritypriority queuequeue.

# Với lệnh type = 2type=2, đây là lệnh yêu cầu ta lấy 11 phần tử ra khỏi cấu trúc dữ liệu đó, nên trước khi thực hiện thao tác này, kiểm tra stackstack, queuequeue, prioritypriority queuequeue có rỗng hay không. Nếu như chúng rỗng mà thao tác này lại bảo mình lấy 11 phần tử ra, thì rõ ràng không thể tồn tại cấu trúc dữ liệu này. Do đó ta gán cả 33 biến đánh dấu là 00 (false).

# Ngược lại, ta kiểm tra phần tử mà ta lấy ra có bằng xx hay không và cập nhật lại biến đánh dấu.

# Kiểm tra các biến đánh dấu và in ra kết quả tương ứng.

# Độ phức tạp: O(NlogN)O(NlogN) với NN là số lượng thao tác. Độ phức tạp sẽ đạt cao nhất khi thao tác trên prioritypriority queuequeue.

import queue
s = []
q = queue.Queue()
pq = queue.PriorityQueue()
 
while True:
    try:
        n = int(input())
    except EOFError:
        break
 
    s.clear()
    q.queue.clear()
    pq.queue.clear()    
    isStack = isQueue = isPQ = True
     
    for _ in range(n):
        type, x = map(int, input().split())
        if type == 1:
            s.append(x)
            q.put(x)
            pq.put(-x)
        else:
            if len(s) == 0:
                isStack = isQueue = isPQ = False
            else:
                if x != s.pop():
                    isStack = False
                if x != q.get():
                    isQueue = False
                if x != -pq.get():
                    isPQ = False
 
    if isStack + isQueue + isPQ == 0:
        print("impossible")
    elif isStack + isQueue + isPQ > 1:
        print("not sure")
    elif isStack:
        print("stack")
    elif isQueue:
        print("queue")
    else:
        print("priority queue")