# # Bạn sẽ bỏ toàn bộ NN số vào hàng đợi ưu tiên, mỗi lần cộng hai số hoặc hai nhóm nào lại với nhau bạn sẽ cộng dồn chi phí lại, đồng thời lấy hai số/nhóm đó ra khỏi hàng đợi. Chi phí mới nhận được lại tiếp tục bỏ vào trong hàng đợi ưu tiên. Khi hàng đợi ưu tiên không còn số nào thì kết quả cộng các chi phí lại sẽ là kết quả cần tìm.
# Tóm tắt đề:

# Cho NN số nguyên, hãy tính chi phí để cộng toàn bộ các số nguyên này lại sao cho chi phí nhỏ nhất. Các số nguyên được cộng mỗi lần cộng hai số riêng lẻ với nhau và lưu lại chi phí, hoặc có thể cộng một số vào một nhóm số đã được cộng trước đó, hoặc cũng có thể hai nhóm cộng lại với nhau

import queue
pq = queue.PriorityQueue()

while True:
    n = int(input())
    
    if n == 0:
        break

    for x in input().split():
        pq.put(int(x))
    
    ans = 0
    
    while pq.qsize() > 1:
        a = pq.get()
        b = pq.get()
        ans += a + b
        pq.put(a + b)

    print(ans)
    pq.get()