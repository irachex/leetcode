'''
https://leetcode.com/problems/string-to-integer-atoi/

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        n = len(str)
        sign = 1
        x = 0
        i = 0
        while i < n and str[i] == ' ':
            i += 1
        if i < n and str[i] == '-':
            sign = -1
            i += 1
        elif i < n and str[i] == '+':
            sign = 1
            i += 1
        while i < n:
            c = str[i]
            if c >= '0' and c <= '9':
                x = x * 10 + int(c)
            else:
                break
            i += 1
        while i < n and str[i] == ' ':
            i += 1
        if sign == 1:
            x = min(x, INT_MAX)
        else:
            x = min(x, -INT_MIN)
        return sign * x


if __name__ == '__main__':
    f = Solution().myAtoi
    assert f('  +123  ') == 123
    assert f('+123') == 123
    assert f('-123') == -123
    assert f(' -123 ') == -123
    assert f('321') == 321
    assert f('  321 ') == 321
    assert f('0') == 0
    assert f('.12') == 0
    assert f('-+12') == 0
    assert f('+-12') == 0
    assert f('+') == 0
    assert f('+  ') == 0
    assert f('   -  ') == 0
    assert f('1+2') == 1
    assert f('1.2') == 1
    assert f('1 2') == 1
    assert f('1ab2') == 1
    assert f("  -0012a42") == -12
    assert f("2147483648") == 2147483647  # XXX: prevent overflow in C
    assert f("-2147483648") == -2147483648
