# coding: utf-8

'''
https://leetcode.com/problems/guess-number-higher-or-lower-ii/

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
'''


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = [[0 for j in xrange(n + 2)] for i in xrange(n + 2)]
        for L in xrange(2, n + 1):
            for i in xrange(1, n - L + 2):
                j = i + L - 1
                d[i][j] = 1 << 31
                for k in xrange(i, j + 1):
                    d[i][j] = min(d[i][j], max(d[i][k - 1], d[k + 1][j]) + k)
        return d[1][n]


if __name__ == '__main__':
    f = Solution().getMoneyAmount
    assert f(1) == 0
    assert f(3) == 2
    assert f(4) == 4
    assert f(7) == 10
    assert f(10) == 16
    print f(20)
