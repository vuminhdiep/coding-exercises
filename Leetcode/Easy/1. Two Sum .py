class Solution(object):


    # Function to find a pair in an array with a given sum using sorting
    def two_sum(self, nums, target):

        # sort the list in ascending order
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))

        # maintain two indices pointing to endpoints of the list
        (low, high) = (0, len(sorted_nums) - 1)

        # reduce the search space `A[low…high]` at each iteration of the loop

        # loop till the search space is exhausted
        while low < high:
            n, k = sorted_nums[low]
            m, l = sorted_nums[high]
            if n + m == target:  # target found
                return [k, l]

            # increment `low` index if the total is less than the desired sum;
            # decrement `high` index if the total is more than the desired sum
            if n + m < target:
                low = low + 1
            else:
                high = high - 1

        # No pair with the given sum exists
        print("Pair not found")

if __name__ == '__main__':
    s = Solution()
    print(s.two_sum([2, 7, 11, 15], 9))
    print(s.two_sum([3, 2, 4], 6))
    print(s.two_sum([3, 3], 6))
    



     
  # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
# Complexity: O(n)
# Hashing
# The key to the problem is that there is ALWAYS only 1 pair of numbers that satisfy the condition of adding together to be the target value.
# We can assume that for all the numbers in the list (x1, x2, ... xn) that there exists a pair such that xa + xb = target
# To solve this with a single pass of the list we can change the equation above to xa = target - xb and since we know the target as long as we maintain a record of all previous values in the list we can compare the current value (xa) to it's ONLY pair, if it exists, in record of all previous values (xb)
# To keep a record of the previous values and their indices I have used a dictionary. Commonly known as a map in other languages. This allows me to record each previous number in the dictionary alongside the indice as a key value pair (target-number, indice).
#         res = {}
#         for i in range(len(nums)):
#             second = target - nums[i]
#             if second in res:
#                 return [res[second], i]
#             else:
#                 res[nums[i]] = i



# Brute force
#Complexity: O(n^2)
        # for i in range(len(nums)):
        #     for j in range(1,len(nums)):
        #         if nums[j] == target - nums[i]:
        #             return [i, j]
