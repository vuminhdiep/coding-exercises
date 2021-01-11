# Bear and Game https://codeforces.com/problemset/problem/673/A

n = int(input())
v = list(map(int, input().split()))

start = 0
watch = 0
for i in v:
    if i - start <= 15:
        watch = i
        start = i
    else:
        break

print(min(90, watch + 15))