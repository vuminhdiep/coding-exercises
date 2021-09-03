class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        #Two pointer
        #i as the slow run (unique pointer) and j as the fast run (current pointer).
        #Time complexity: O(n)
        #Space complexity: O(1)
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
        return i+1


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0, 1, 1, 2, 3, 4, 4]))

