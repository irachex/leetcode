"""
http://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        ans = 0
        for i in range(len(prices)):
            if i > 0 and prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        return ans


if __name__ == "__main__":
    s = Solution()

    prices = [1, 2, 4]
    assert s.maxProfit(prices) == 3
