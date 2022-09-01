from heapq import *
import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        #Complexity: O(k * logn)
        #use maxheap to keep k points
        maxHeap = []
        res = []
        for point in points:
            distance = sqrt(point[0] * point[0] + point[1] * point[1]) * (-1) #python default min heap so have to multiply (-1)
            heapq.heappush(maxHeap, [distance, point])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap) #keep the k closest point in the heap
            
        while len(maxHeap) > 0:
            popped = heapq.heappop(maxHeap)
            res.append(popped[1]) #get the k closest point
        return res
        