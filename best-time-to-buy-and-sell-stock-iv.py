'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''


class Solution(object):

    def maxProfit(self, k, prices):  # O(kn) in worst case
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        if k >= n / 2:
            ans = 0
            for i in xrange(1, n):
                if prices[i] > prices[i - 1]:
                    ans += prices[i] - prices[i - 1]
            return ans
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
    assert f(2, [1, 4, 2]) == 3
