from heapq import *
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
      #use minHeap to store number, diff
      #pop to keep k elements in minHeap
      #return first element in minHeap
     
      #complexity: O(nlogn) time, O(n) space 

        minHeap = []
        for num in arr:
            heappush(minHeap, (abs(num - x), num))
        res = []
        for i in range(k):
            res.append(heappop(minHeap)[1])
        res.sort()
        return res
    


