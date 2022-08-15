class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        #return the product of first three numbers in the array
        #Complexity: O(nlogn) time, O(1) space
        first_3 = nums[-1] * nums[0] * nums[1] #First two smallest negative numbers, with one largest positive number.
        last_3 = nums[-1] * nums[-2] * nums[-3] #First three largest positive numbers
        max_prod = max(first_3, last_3)
        return max_prod