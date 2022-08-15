class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Binary search
        #Complexity: O(logn) time, O(1) space
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[mid + 1]: #peak in second half
                start = mid + 1
            else:
                end = mid
        
        #when start == end which is peak
        return start