# Nhận xét:

# Có thể mô phỏng thao tác rút lá bài ra tương tự như thao tác lấy dữ liệu từ queue và đưa lá bài vào giống như thêm dữ liệu vào queue (lá bài được thêm vào sẽ nằm ở cuối).

# Ta có các bước thực hiện để giải bài toán như sau:

# Bước 1: Đưa hết các lá bài theo thứ tự từ 11 đến NN vào CTDL queue.
# Bước 2: Khi số lượng lá bài trong queue còn ít nhất hai lá:
# Lấy lá bài trên đầu queue ra.
# Lấy lá bài mới trên đầu queue ra và đưa lại vào cuối queue.
# Bước 3: In ra kết quả theo định dạng trong các ví dụ.
# Bước 4: Reset các biến cần thiết, chuẩn bị cho bộ test tiếp theo.
# Lưu ý: Cần cẩn thận trong cách trình bày kết quả. 
# Với trường hợp không rút được lá bài nào ra khỏi chồng bài (N = 1)(N=1), ta chỉ in ra "Discarded cards:" nhưng không có khoảng trắng ở cuối.

import queue
deck = queue.Queue()
 
while True:
    n = int(input())
    if n == 0:
        break
 
    for i in range(1, n + 1):
        deck.put(i)
 
    discarded_cards = []
      
    while deck.qsize() >= 2:
        discarded_cards.append(deck.get())
        deck.put(deck.get())
     
    print('Discarded cards: ' if discarded_cards else 'Discarded cards:', end='')
    print(*discarded_cards, sep=', ')
    print('Remaining card: {}'.format(deck.get()))
