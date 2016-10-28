'''
https://leetcode.com/problems/add-strings/

Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = []
        r = 0
        len1 = len(num1)
        len2 = len(num2)
        for i in xrange(max(len1, len2)):
            n1 = int(num1[len1 - i - 1]) if i < len1 else 0
            n2 = int(num2[len2 - i - 1]) if i < len2 else 0
            x = n1 + n2 + r
            if x >= 10:
                x -= 10
                r = 1
            else:
                r = 0
            ans.append(x)
        if r:
            ans.append(r)
        return ''.join(map(str, reversed(ans)))


if __name__ == '__main__':
    f = Solution().addStrings
    assert f('0', '0') == '0'
    assert f('1', '9') == '10'
    assert f('1234', '58') == str(1234 + 58)
    assert f('2134', '1234435') == str(2134 + 1234435)
