class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([0, 1, 1, 2, 3, 4, 4], 4))


