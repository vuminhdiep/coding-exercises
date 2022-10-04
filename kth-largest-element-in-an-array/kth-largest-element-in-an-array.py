from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #create a max heap
        #pop i k times
        #return the top element
        #Complexity: O(logK) time, O(k) space 
        res = 0
        maxHeap = []
        for i in nums:
            heapq.heappush(maxHeap, -i)
        for j in range(k-1):
            heapq.heappop(maxHeap)
        res = -maxHeap[0]
        return res
        