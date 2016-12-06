# coding: utf-8

'''
https://leetcode.com/problems/remove-k-digits/

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        a = map(int, num)
        stack = []
        for i in xrange(len(a)):
            while stack and k > 0 and stack[-1] > a[i]:
                k -= 1
                stack.pop()
            stack.append(a[i])
        while stack and k > 0:
            k -= 1
            stack.pop()
        return ''.join(map(str, stack)).lstrip('0') or '0'


if __name__ == '__main__':
    f = Solution().removeKdigits
    assert f('1432219', 3) == '1219'
    assert f('10200', 1) == '200'
    assert f('10', 2) == '0'
    assert f('9', 1) == '0'
