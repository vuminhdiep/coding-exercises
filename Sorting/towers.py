# https://codeforces.com/problemset/problem/37/A

n = int(input())
l = list(map(int, input().split()))
l.sort()
n_towers = 1
max_height = 1
cur_height = 1
for i in range(1,n):
    if l[i]==l[i-1]:
        cur_height+=1
        max_height = max(max_height, cur_height)
    else:
        n_towers+=1
        cur_height=1

print(max_height,n_towers)