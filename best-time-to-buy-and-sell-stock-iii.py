'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        k = 2
        d = [[0 for j in xrange(n)] for i in xrange(k + 1)]
        for t in xrange(1, k + 1):
            max_d = -(1 << 31)
            for i in xrange(n):
                # d[t][i] = max(d[t][i], d[t][i - 1], d[t - 1][j] + prices[i] - prices[j])
                d[t][i] = max(d[t][i], d[t][i - 1], max_d + prices[i])
                max_d = max(max_d, d[t - 1][i] - prices[i])
        return d[k][n - 1]


if __name__ == '__main__':
    f = Solution().maxProfit
    assert f([1, 4, 2]) == 3
