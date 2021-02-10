# Ta dựa vào một nhận xét như sau: Khi HH càng tăng, rõ ràng tổng lượng gỗ bị chặt sẽ càng giảm và ngược lại. Do đó, nếu giả sử như ta có thể quy định midmid là độ dài của các khúc gỗ mà sau khi chặt không được phép vượt quá midmid. Nếu như tổng lượng gỗ bị chặt mà ≥ M, điều này có nghĩa rằng đáp án của ta có thể là mid, hoặc đáp án của ta sẽ nằm trong đoạn từ mid + 1mid+1 trở về sau. Còn nếu tổng lượng gỗ bị chặt mà < M<M thì rõ ràng ta không thể nào nhận mid làm đáp án được mà phải tìm từ mid - 1mid−1 trở về trước. Từ ý tưởng này, ta hình thành nên thuật toán chặt nhị phân như sau:
#
# Gọi getSum(x)getSum(x) là tổng lượng gỗ bị chặt khi ta quy định độ dài của các cây sau khi chặt không được vượt quá xx.
# Ta đặt l = 0l=0, r = 10^9 + 10 đại diện cho trường hợp xấu nhất là chặt hết gỗ vẫn không đủ và trường hợp tốt nhất là không cần chặt cây nào.
# Trong lúc l ≤ r, ta đặt mid = (l + r) / 2mid=(l+r)/2, nếu getSum(mid) >= MgetSum(mid)>=M thì ta tiến hành cập nhật res = midres=mid, đồng thời tìm kết quả tiếp trên đoạn [mid + 1, r][mid+1,r], tức gán l = mid + 1l=mid+1. Ngược lại, nếu getSum(mid) < MgetSum(mid)<M thì ta tìm kết quả trên đoạn [l...mid - 1][l...mid−1], tức gán r = mid - 1r=mid−1.
# Độ phức tạp: O(Nlog(max(hi))O(Nlog(max(hi)) với NN là số lượng cây và max(hi)max(hi) là chiều cao lớn nhất của cây.


import sys

def inp():
    return map(int, input().split(' '))

def check(a, x):
    sum = 0
    for item in a:
        sum += max(0, item - x)
    return sum

def BS_search(a, l, r, k):
    ans = r
    while l <= r:
        mid = int( (l + r) / 2 )
        if check(a, mid) >= k:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

def solve():
    n, k = inp()
    a = list(inp())
    vmin = 0
    vmax = 1e9
    print (BS_search(a, vmin, vmax, k))

solve()