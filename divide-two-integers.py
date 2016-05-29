'''
https://leetcode.com/problems/divide-two-integers/

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = (1 << 31) - 1
        MIN_INT = -(1 << 31)
        if divisor == 0 or dividend == MIN_INT and divisor == -1:
            return MAX_INT

        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor
        p = divisor
        q = 1
        while p + p <= dividend:
            p <<= 1
            q <<= 1
        r = 0
        while dividend >= divisor:
            if dividend >= p:
                dividend -= p
                r = r | q
            p >>= 1
            q >>= 1
        return r if sign > 0 else -r


if __name__ == '__main__':
    f = Solution().divide
    assert f(10, 5) == 2
    assert f(10, 3) == 3
    assert f(3, 10) == 0
    assert f(10, -2) == -5
    assert f(10, 2) == 5
    assert f(-2147483648, -1) == 2147483647
