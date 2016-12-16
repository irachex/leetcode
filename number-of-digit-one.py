'''
https://leetcode.com/problems/number-of-digit-one/

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

Beware of overflow.
'''


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        m = 1
        while m <= n:
            left, right = n / m, n % m
            x = left % 10
            if x == 0:
                ans += left / 10 * m  # 0..left/10-1
            elif x == 1:
                ans += left / 10 * m + right + 1  # 0..left/10 + 0..right
            else:
                ans += (left / 10 + 1) * m
            m *= 10
        return ans


if __name__ == '__main__':
    def g(n):
        return sum(str(i).count('1') for i in xrange(n + 1))

    f = Solution().countDigitOne
    assert f(100) == g(100), g(100)
    assert f(1) == 1
    assert f(13) == g(13)
    assert f(23) == g(23)
    assert f(374) == g(374)
    assert f(118) == g(118), g(118)
    assert f(218) == g(218), g(218)
