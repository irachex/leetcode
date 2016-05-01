'''
https://leetcode.com/problems/excel-sheet-column-title/

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        while n > 0:
            x = (n - 1) % 26 + 1
            s = chr(x + 64) + s
            n = (n - 1) / 26
        return s


if __name__ == '__main__':
    f = Solution().convertToTitle
    assert f(52) == 'AZ'
    assert f(26) == 'Z'
    assert f(28) == 'AB'
    assert f(53) == 'BA'
