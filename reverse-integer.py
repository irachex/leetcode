"""
http://oj.leetcode.com/problems/reverse-integer/

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0:
            return 0
        sign = x / abs(x)
        return sign * int(str(abs(x))[::-1])
