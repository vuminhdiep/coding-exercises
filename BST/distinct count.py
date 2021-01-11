t = int(input())
for i in range(t):
    n, x = list(map(int, input().split()))
    arr = input().split()
    arr = set(arr)
    if len(arr) == x:
        print('Good')
    elif len(arr) < x:
        print('Bad')
    elif len(arr) > x:
        print('Average')