# Hướng dẫn giải: Do yêu cầu của khuyến mãi là lấy phiếu có giá trị lớn nhất và nhỏ nhất nên ta có thể sử dụng 2 heap đồng thời:

# Max-heap với top là phiếu có giá trị lớn nhất
# Min-heap với top là phiếu có giá trị nhỏ nhất Theo quy định phiếu đã lấy ra thì không bỏ lại vào thùng nên sau khi tính được số tiền phải chi trong ngày của siêu thị bằng cách trừ top của max-heap và min-heap, ta tiến hành pop cả hai phiếu này ra khỏi hàng đợi và tiếp tục xử lý phiếu của những ngày tiếp theo.
# Tuy nhiên nếu chỉ làm như vậy thì các phiếu được lấy ra từ max-heap có thể còn trong min-heap và ngược lại. Do đó ta cần đánh dấu lại các phiếu đã được lấy ra khỏi thùng để về sau khi lấy phiếu ra ta bỏ qua những phiếu đã được lấy ra trước đó rồi. Một cách đơn giản để đánh dấu các phiếu đã được lấy ra rồi là ta sẽ đánh dấu dựa trên số thứ tự đơn hàng.

import heapq

taken = [False] * 1000005
maxHeap = []
minHeap = []
money = 0
nbills = 0

n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    
    for x in a[1:]:
        nbills += 1
        heapq.heappush(maxHeap, (-x, nbills))
        heapq.heappush(minHeap, (x, nbills))

    while taken[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
    
    while taken[minHeap[0][1]]:
        heapq.heappop(minHeap)
    
    taken[maxHeap[0][1]] = taken[minHeap[0][1]] = True
    money += -heapq.heappop(maxHeap)[0] - heapq.heappop(minHeap)[0]

print(money)