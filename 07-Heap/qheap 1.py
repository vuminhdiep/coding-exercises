from heapq import heappush, heappop

n = int(input())
heap = []
lookup = set()
for i in range(n):
    q = list(map(int, input().split()))
    if q[0] == 1:
        heappush(heap, q[1])
        lookup.add(q[1])

    elif q[0] == 2:
        lookup.discard(q[1])
    else:
        while heap[0] not in lookup:
            heappop(heap)

        print(heap[0])