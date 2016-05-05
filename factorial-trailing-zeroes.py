'''
https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        x = 5
        while x <= n:
            ans += n / x
            x *= 5
        return ans


if __name__ == '__main__':
    f = Solution().trailingZeroes
    assert f(7) == 1
    assert f(10) == 2
    assert f(20) == 4
    assert f(27) == 6
    assert f(50) == 12
