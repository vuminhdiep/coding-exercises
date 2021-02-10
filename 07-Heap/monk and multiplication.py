import heapq

N = int(input())

arr = list(map(int, input().split()))

heap = []

for i in arr:

    heapq.heappush(heap, -i)

    if len(heap) < 3:
        print(-1)

        continue

    largest = heapq.heappop(heap)

    second_largest = heapq.heappop(heap)

    third_largest = heapq.heappop(heap)

    print(-1 * largest * second_largest * third_largest)

    heapq.heappush(heap, largest)

    heapq.heappush(heap, second_largest)

    heapq.heappush(heap, third_largest)