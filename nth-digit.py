'''
https://leetcode.com/problems/nth-digit/

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
Input:
3
Output:
3

Example 2:
Input:
11
Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 9
        lower = 1
        digit = 1
        while n > num * lower * digit:
            n -= num * lower * digit
            lower *= 10
            digit += 1
        x = lower + (n - 1) / digit if n > 0 else lower
        p = (n - 1) % digit if n > 0 else 0
        return x / (10 ** (digit - p - 1)) % 10


# 1 .. 9                9 digits
# 10 .. 99         90 * 2 digits
# 100 ... 999     900 * 3 digits


if __name__ == '__main__':
    f = Solution().findNthDigit
    assert f(100) == 5
    assert f(11) == 0
    assert f(12) == 1
    assert f(120) == 6
