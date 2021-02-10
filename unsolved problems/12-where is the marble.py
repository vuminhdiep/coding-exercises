# Đầu tiên sắp xếp lại mảng tăng dần. Sau đó sử dụng hàm lower\_boundlower_bound hoặc tự cài đặt hàm BSFirst để tìm vị trí đầu tiên XX xuất hiện trong mảng.
# Complexity: O(T∗Q∗logN) với TT là số lượng test, QQ là số lượng truy vấn, NN là số lượng viên bi.

def inp():
    return map(int, input().split(' '))


def bsFirst(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid - 1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return bsFirst(a, mid + 1, right, x)
        else:
            return bsFirst(a, left, mid - 1, x)
    return -1


def BS_search(a, l, r, value):
    ans = -1
    while l <= r:
        mid = int((l + r) / 2)
        if a[mid] == value:
            ans = mid
            r = mid - 1
        elif a[mid] > value:
            r = mid - 1
        else:
            l = mid + 1
    return ans


def solve():
    testcase = 0
    while True:
        testcase += 1
        n, q = inp()
        if n == 0 and q == 0:
            break
        a = []
        for i in range(n):
            x = int(input())
            a.append(x)
        a.sort()
        print("CASE# " + str(testcase) + ":")
        for i in range(q):
            x = int(input())
            ans = bsFirst(a, 0, n - 1, x)
            if ans == -1:
                print(str(x) + " not found")
            else:
                print(str(x) + " found at " + str(ans + 1))


solve()
