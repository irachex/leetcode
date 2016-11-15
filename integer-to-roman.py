#coding: utf-8

'''
http://oj.leetcode.com/problems/integer-to-roman/

Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @return a string
    def intToRoman(self, num):
        digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                  (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                  (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        s = ''
        i = 0
        while i < len(digits):
            val, c = digits[i]
            if num < val:
                i += 1
            else:
                num -= val
                s += c
        return s


if __name__ == "__main__":
    s = Solution()
    assert s.intToRoman(19) == 'XIX'
    assert s.intToRoman(79) == 'LXXIX'
    assert s.intToRoman(707) == 'DCCVII'
    assert s.intToRoman(1800) == 'MDCCC'
