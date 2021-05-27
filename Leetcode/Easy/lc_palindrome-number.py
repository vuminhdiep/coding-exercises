class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #Reverse the number and check if the reversed number == original number
        #Have to assign the orginial number to another variable in order to reverse
        if x < 0:
            return False
        p = x
        res = 0
        while p:
            remain = p%10 
            res = res*10 + remain
            p = p//10 
        
        return res == x

if __name__ == '__main__':
    s = Solution()
    s.isPalindrome(121)
    s.isPalindrome(-121)
    s.isPalindrome(10)
    s.isPalindrome(-101)

