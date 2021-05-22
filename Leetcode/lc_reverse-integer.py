
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        #Push and pop
#         //pop operation:
#           pop = x % 10;
#           x /= 10;

#          //push operation:
#            temp = rev * 10 + pop;
#            rev = temp;
        neg_or_pos = -1 if x < 0 else 1
        x = x*neg_or_pos

        res = 0
        while x > 0:
            remain = x%10 #Find the remainder
            res = res*10 + remain
            x = x//10 #Find the quotient
        return 0 if res > pow(2,31) else res*neg_or_pos

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-120))

