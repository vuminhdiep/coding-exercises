# https://codeforces.com/problemset/problem/557/B

n,w = map(int,input().split())
a = sorted(list(map(int, input().split())))
x = min(a[0],a[n]/2)
print(min(w,x*n*3))