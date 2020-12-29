k,n,w=map(int,input().split())
cost = (k * w * (w + 1)) // 2
if cost <= n:
    print(0)
else:
    print(cost - n)