# https://codeforces.com/problemset/problem/387/B

n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(j) for j in input().split()]
pointer_a = 0
pointer_b = 0
while pointer_a < n and pointer_b < m:
    if a[pointer_a] <= b[pointer_b]: #Lack of number with complexity b
        pointer_a+=1
    pointer_b+=1
print(n-pointer_a) #Print out the needed problems