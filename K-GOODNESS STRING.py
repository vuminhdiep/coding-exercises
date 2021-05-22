import math
t = int(input())

for j in range(t):
    score = 0
    res = 0
    n, k = map(int, input().split())
    s = input()

    for i in range(1,math.floor(n/2-1)):
        if s[i] != s[n-i+1]:
            score += 1
    if score != k:
        res += 1
    else:
        res = 0
    text = "Case #{0}: {1}".format(j+1,res)
    print(text)