# https://leetcode.com/problems/missing-number/
#Cach 1
def missingNumber(nums):
    res = 0
    nums.sort()
    for i in range(len(nums)):
        if i != nums[i]:
            res = i
        elif i == len(nums) - 1 and i == nums[i]:
            res = i + 1

    return res


arrays = [0]
print(missingNumber(arrays))

#Cach 2:
def missingNum(nums):
    n = len(nums)
    sumN = n * (n+1) //2
    return sumN - sum(nums)

#Cach 3
# XOR: 1 ^ 0 = 1
#      0 ^ 0 = 0
#      1 ^ 1 = 0