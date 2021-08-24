class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])
        return profit


if __name__ == '__main__':
    prices = []
    prices = [int(price) for price in input().split()]
    s = Solution()
    print(s.maxProfit(prices))
