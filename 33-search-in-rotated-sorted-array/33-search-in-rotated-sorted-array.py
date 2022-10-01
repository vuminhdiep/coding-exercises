class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #binary search
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]: #if first half is non rotated
                if target >= nums[left] and target < nums[mid]: #target is in left half, non-rotated part
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and target > nums[mid]: #target in right half, non-rotated part
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 #if not found target
                    
        