# Arrays https://codeforces.com/problemset/problem/572/A

nA, nB = (map(int, input().split()))
k, m = (map(int, input().split()))

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

if listA[k-1] < listB[nB-m]: #if first k numbers in A < last m number in B
    print("YES")
else:
    print("NO")