'''
https://leetcode.com/problems/multiply-strings/

Given two numbers represented as strings, return multiplication of the numbers as a string.
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n = len(num1)
        m = len(num2)
        a = [0 for i in xrange(n + m + 1)]
        for i, c1 in enumerate(reversed(num1)):
            for j, c2 in enumerate(reversed(num2)):
                a[i + j] += int(c1) * int(c2)
        s = ''
        for i in xrange(n + m + 1):
            if a[i] >= 10:
                a[i + 1] += a[i] / 10
                a[i] = a[i] % 10
            s = str(a[i]) + s
        return s.lstrip('0') or '0'

if __name__ == '__main__':
    f = Solution().multiply
    print f('1', '0')
    print f('4', '4')
    print f('25', '1125')
