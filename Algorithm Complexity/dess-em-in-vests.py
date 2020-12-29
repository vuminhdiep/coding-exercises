# https://codeforces.com/problemset/problem/161/A

n, m, x, y = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(j) for j in input().split()]
l = []
i = 0
j = 0
while j < len(b) and i < len(a):
    if a[i] - x <= b[j] <= a[i] + y:
        l.append((i + 1, j + 1))  # Add people with fit vest starting from index 1
        j += 1
        i += 1
    elif b[j] > a[i] + y:
        i += 1
    elif b[j] < a[i] + x:
        j += 1
print(len(l)) #Number of maximum people
for k in l:
    print(k[0], k[1])