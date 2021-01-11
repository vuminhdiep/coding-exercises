# https://codeforces.com/problemset/problem/381/A

n = int(input())
l = [int(k) for k in input().split()]
s = 0
d = 0
for i in range(n):
    draw_card = max(l[0],l[-1])
    if i%2==0:
        s+=draw_card
    else:
        d+=draw_card
    l.remove(draw_card)
print(s,d)
