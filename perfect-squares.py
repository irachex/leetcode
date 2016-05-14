'''
https://leetcode.com/problems/perfect-squares/

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''

class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = []
        i = 1
        while i * i <= n:
            a.append(i * i)
            i += 1
        reach = set([0])
        level = 0
        while True:
            level += 1
            next_reach = set()
            for x in a:
                for i in reach:
                    if i + x == n:
                        return level
                    next_reach.add(i + x)
            reach = next_reach
        return n

    def numSquares_DP(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = []
        i = 1
        while i * i <= n:
            a.append(i * i)
            i += 1
        d = [n for i in xrange(n + 1)]
        d[0] = 0
        for x in reversed(a):
            for j in xrange(x, n + 1):
                d[j] = min(d[j], d[j - x] + 1)
        return d[n]

    def numSquares_math(self, n):
        # there is a math solution
        pass


if __name__ == '__main__':
    f = Solution().numSquares
    assert f(9611) == 3
    assert f(5673) == 3
    assert f(16) == 1
    assert f(12) == 3
    assert f(13) == 2
