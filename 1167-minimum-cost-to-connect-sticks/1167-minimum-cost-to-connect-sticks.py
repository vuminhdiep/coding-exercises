from heapq import *
class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        #Complexity: O(n * logn) time, O(n) space
        #use minHeap to store smallest stick length
        minHeap = []
        for stick in sticks:
            heapq.heappush(minHeap, stick)
        res = 0
        temp = 0
        while len(minHeap) > 1:
            temp = heapq.heappop(minHeap) + heapq.heappop(minHeap) #add the two smallest stick lengths together
            res += temp
            heapq.heappush(minHeap, temp)
        return res
        