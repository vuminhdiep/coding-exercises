t=int(input())
for i in range(t):
    n,m=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    dic=set()
    for i in range(n):
        dic.add(arr[i])
    for i in range(n,n+m):
        if arr[i] in dic:
            print("YES")
        else:
            print("NO")
        dic.add(arr[i])