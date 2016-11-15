#coding: utf-8

'''
http://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        INF = 999999999
        min_price = INF
        ans = 0
        for p in prices:
            ans = max(ans, p - min_price)
            min_price = min(min_price, p)
        return ans
