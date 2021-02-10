n = int(input())
h = [int(i) for i in input().split()]
s = sorted([(h[i], i) for i in range(n)])
f = [s[i][1] for i in range(n)]
swp = []

for i in range(n-1):
    if s[i][0] == s[i+1][0]:
        swp.append((i,i+1))
    if len(swp)==2:
        print('YES')
        print(' '.join(str(k+1) for k in f))
        for i,j in swp:
            f[i],f[j]=f[j],f[i]
            print(' '.join(str(l+1) for l in f))
        exit()
print('NO')