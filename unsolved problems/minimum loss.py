# Với mỗi năm, gọi pp là giá tiền của ngôi nhà lớn hơn giá ở năm thứ ii (a[i]a[i]) nhưng là giá nhỏ nhất trong các năm từ năm 11 đến năm i – 1. Nếu tìm được pp thì cập nhật lại res = min(res , p – a[i]). Để có thể thực hiện được việc tìm pp, bạn bỏ các phần tử từ phần tử 1 đến phần tử i – 1 vào một cây nhị phân tìm kiếm. Sau đó, với mỗi phần tử a[i], sử dụng hàm tìm phần tử nhỏ nhất lớn hơn a[i] để tìm ra được pp.

class Node:
   def __init__(self, value):
      self.value = value
      self.left = self.right = None

def insert(root, x):
   if root is None:
      return Node(x)
   if x < root.value:
      root.left = insert(root.left, x)
   elif x > root.value:
      root.right = insert(root.right, x)
   return root

def upperbound(root, x):
   if root is None:
      return root
   if root.value <= x:
      return upperbound(root.right, x)
   elif root.value > x:
      ub_left = upperbound(root.left, x)
      return root if ub_left is None else ub_left

n = input()
prices = list(map(int, input().split()))

minimum_loss = 10 ** 16
root = None

for sell_price in prices:
   best_buy_node = upperbound(root, sell_price)
   if best_buy_node is not None:
      minimum_loss = min(best_buy_node.value - sell_price, minimum_loss)
   root = insert(root, sell_price)

print(minimum_loss)