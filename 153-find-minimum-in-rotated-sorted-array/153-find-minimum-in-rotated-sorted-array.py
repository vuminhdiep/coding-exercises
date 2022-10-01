class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #use binary search
        #Complexity: O(logn) times, O(1) space
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        #if not rotated: last element > first element in array => smallest element is first
        if nums[right] > nums[0]:
            return nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]: #found the pivot and the minimum element is in right half
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]: #found the pivot and the minimum element is in left half
                return nums[mid]
            
            if nums[mid] > nums[0]: #the minimum element in right half
                left = mid + 1
            else:
                right = mid - 1 #the minimum in left half
        return nums[left]
                
        