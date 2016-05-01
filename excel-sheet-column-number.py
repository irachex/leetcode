'''
https://leetcode.com/problems/excel-sheet-column-number/

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        for i, c in enumerate(reversed(s)):
            r += (ord(c) - ord('A') + 1) * (26 ** i)
        return r


if __name__ == '__main__':
    f = Solution().titleToNumber
    assert f('A') == 1
    assert f('AA') == 27
    assert f('AB') == 28
