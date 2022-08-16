from heapq import *
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        #use max heap to get the first two stones which are heaviest
        #add the remaining weight != 0 to the heap
        #continuously pop left until the heap only has 1 item 
        #Complexity: O(nlogn) time for heappush, O(n) space
        heap = []
        for i in stones:
            heapq.heappush(heap,-i) # Using as max heap.
        while len(heap) > 1:
            x = heapq.heappop(heap) # x and y are top 2 largest values.
            y = heapq.heappop(heap)
            heapq.heappush(heap,x-y)
        ans = heapq.heappop(heap) #revert back to positive
        return -ans