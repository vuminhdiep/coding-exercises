n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

left = 0
right = a[-1]

for i in range(100):
    mid = (left + right) / 2.0

    s1 = sum([x - mid for x in a if x >= mid]) * (100 - k) / 100.0
    s2 = sum([mid - x for x in a if x < mid])

    if s1 >= s2:
        left = mid
    else:
        right = mid

print(left)