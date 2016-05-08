'''
https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = amount + 1
        d = [MAX for i in xrange(amount + 1)]
        d[0] = 0
        for i, x in enumerate(coins):
            for j in xrange(x, amount + 1):
                d[j] = min(d[j], d[j - x] + 1)
        return d[amount] if d[amount] < MAX else -1


if __name__ == '__main__':
    f = Solution().coinChange
    assert f([1, 2, 5], 11) == 3
    assert f([2], 3) == -1
