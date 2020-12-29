# Big Segment https://codeforces.com/problemset/problem/242/B
n = int(input())
m = []
for i in range(n):
    a, b = map(int, input().split())
    m.append([a, b])

min_val = min([x[0] for x in m]) #Get the smallest value possible in the segments
max_val = max([x[1] for x in m]) #Get the biggest value possible in the segments
seg = [min_val, max_val] #The segment with smallest and biggest value will cover all segments in between
if seg in m:
    print(m.index(seg) + 1)
else:
    print(-1)
