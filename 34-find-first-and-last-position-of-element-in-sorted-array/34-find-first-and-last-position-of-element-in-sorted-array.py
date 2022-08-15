class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Complexity: O(logn) time, O(1) space
        
        res = [-1, -1]
        res[0] = self.binary_search(nums, target, False) #first index of target
        if res[0] != -1:
            res[1] = self.binary_search(nums, target, True)
        return res
    
    def binary_search(self, nums, target, maxIndex):
        index = -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (end + start) // 2
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else: #when nums[mid] == target
                index = mid
                if maxIndex:
                    start = mid + 1 #search ahead the last index of target
                else:
                    end = mid - 1 #search behind the first index of target
        return index