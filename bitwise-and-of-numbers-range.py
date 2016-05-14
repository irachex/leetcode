'''
https://leetcode.com/problems/bitwise-and-of-numbers-range/

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
'''

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        p = 1
        while m != n:
            m >>= 1
            n >>= 1
            p <<= 1
        return m * p


if __name__ == '__main__':
    f = Solution().rangeBitwiseAnd
    assert f(0, 0) == 0
    assert f(3, 4) == 0
    assert f(1, 2) == 0
    assert f(5, 7) == 4
