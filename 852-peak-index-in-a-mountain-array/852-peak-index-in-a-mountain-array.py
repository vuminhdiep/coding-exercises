class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #Complexity: O(logn) time, O(1) space
        start = 0
        end = len(arr) - 1
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] < arr[mid + 1]: #peak index in the second half
                start = mid + 1
            else:
                end = mid 
        return start #when start == end which is at peak index
        