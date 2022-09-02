from heapq import *
class KthLargest(object):
    #complexity: O(n*logn) time, O(n) space
    

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.minHeap = [] #use minheap to store the numbers because lowest value at the top so after popping the k largest will be the first element
        for num in nums:
            heapq.heappush(self.minHeap, num)
        while len(self.minHeap) > k: #only keep the k largest element in the heap
            heapq.heappop(self.minHeap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        res = self.minHeap[0]
        return res
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)