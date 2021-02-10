n=int(input())
string=input().lower()
x=set([string[i] for i in range(n)])
if len(x)==26:
    print("YES")
else:
    print("NO")