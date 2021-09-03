class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()

        for i in range(len(nums)):

            if nums[i] in num_set:
                return nums[i]
            else:
                num_set.add(nums[i])

        return -1
