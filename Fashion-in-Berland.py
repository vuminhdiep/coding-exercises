# Fashion in Berland: https://codeforces.com/problemset/problem/691/A

def check_jacket(v, n):
    # 1-button jacket
    if n == 1:
        if v[0] == 1:
            return True
        else:
            return False
    count = 0
    for i in range(n):
        if v[i] == 0:
            count += 1

    if count == 1:
        return True
    else:
        return False


n = int(input())
v = list(map(int, input().split()))
if check_jacket(v, n):
    print("YES")
else:
    print("NO")