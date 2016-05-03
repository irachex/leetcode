'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        INF = 1 << 31
        d = [[-INF, -INF, -INF] for i in xrange(n + 1)]
        d[0] = [0, -INF, 0]
        for i in xrange(1, n + 1):
            pi = prices[i - 1]
            d[i][0] = max(d[i - 1][2], d[i - 1][1] + pi)  # sell
            d[i][1] = max(d[i - 1][1], d[i - 1][2] - pi)  # buy
            d[i][2] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2])  # cooldown
        return max(d[n])


if __name__ == '__main__':
    f = Solution().maxProfit
    assert f([1, 2, 3, 0, 2]) == 3
