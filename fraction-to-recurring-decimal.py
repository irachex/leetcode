'''
https://leetcode.com/problems/fraction-to-recurring-decimal/

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
Hint:

No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.
'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = 1
        if numerator < 0:
            sign = -sign
            numerator = -numerator
        if denominator < 0:
            sign = -sign
            denominator = -denominator
        int_part = numerator / denominator
        numerator = numerator % denominator * 10
        p = -1
        r = []
        ns = [numerator]
        while numerator != 0:
            x = numerator / denominator
            r.append(x)
            numerator = numerator % denominator * 10
            try:
                k = ns.index(numerator)
                p = k
                break
            except Exception:
                pass
            ns.append(numerator)
        s = ('-' if sign < 0 and (r or int_part) else '') + str(int_part)
        r = map(str, r)
        if r:
            if p == -1:
                s += '.' + ''.join(r)
            else:
                s += '.' + ''.join(r[:p]) + '(' + ''.join(r[p:]) + ')'
        return s


if __name__ == '__main__':
    f = Solution().fractionToDecimal
    assert f(-2147483648, 1) == '-2147483648'
    assert f(0, -5) == '0'
    assert f(-50, 8) == '-6.25'
    assert f(1, 333) == '0.(003)'
    assert f(1, 2) == '0.5'
    assert f(2, 1) == '2'
    assert f(1, 8) == '0.125'
    assert f(1, 7) == '0.(142857)'
    assert f(2, 3) == '0.(6)'
    assert f(4, 9) == '0.(4)'
    assert f(4, 333) == '0.(012)'
