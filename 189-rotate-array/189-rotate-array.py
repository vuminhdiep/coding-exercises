class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #merge nums[n-k: end] and nums[0:n-k]
        #O(n) time and O(n) space
        n = len(nums)
        rotated_array = [0] * n
        for i in range(n):
            rotated_array[(i + k) % n] = nums[i]
            
        nums[:] = rotated_array #copy the new array to the original one
        return nums
        
        