#https://codeforces.com/problemset/problem/279/B

n,t=map(int,input().split())
l=[int(k) for k in input().split()]
a=j=0
for i in range(n):
    a+=l[i]
    if a>t:
        a-=l[j]
        j+=1
print(n-j)