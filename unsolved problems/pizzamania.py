# Ở đây đề bài yêu cầu ta chia NN số nguyên sao cho được nhiều cặp nhất và mỗi cặp có tổng bằng MM. Vì mọi giá trị trong mảng đều phân biệt, nên hai cặp {a, b} và {c, d} với a + b = c + d = MM thì ta chắc chắn thấy rằng 4 số này đều sẽ khác nhau. Như vậy, có thể sử dụng binary search. Với mỗi giá trị xx, ta sẽ thử tìm yy sao cho xx + yy = MM. Vì vai trò của xx và yy là như nhau, nên ta giả sử xx < yy. Như vậy, bài toán sẽ trở thành với mỗi phần tử xx ta chỉ cần kiểm tra xem phần tử MM – yy có nằm trong mảng hay không. Tức duyệt lần lượt qua mỗi phần tử, với mỗi a[i]a[i], xem MM – a[i]a[i] có xuất hiện trong mảng con từ ii + 11 đến NN – 11 hay không (index tính từ 0).
#
# Độ phức tạp: O(T * NlogN) với T là số lượng bộ dữ liệu, N là số lượng chiếc bánh pizza.

def BinarySearch(a, left, right, x):
    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            return True
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    return False


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    cnt = 0

    for i in range(n):
        comp = m - a[i]
        if BinarySearch(a, i + 1, n - 1, comp):
            cnt += 1

    print(cnt)