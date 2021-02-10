import math
t = int(input())
for i in range(t):
    n = int(input())
    sqt = math.ceil(math.sqrt(n))
    exit_num = sqt*sqt-n
    row = 0
    col = 0
    if exit_num < sqt:
        row = exit_num+1
        col = sqt
    else:
        row = sqt
        col = n-(sqt-1)*(sqt-1)
    if sqt%2 == 0:
        row,col = col,row

    res = "Case {num}: {r} {c}".format(num=i+1,r=row,c=col)
    print(res)