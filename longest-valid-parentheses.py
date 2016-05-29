'''
https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = [0 for i in xrange(len(s))]
        for i, c in enumerate(s):
            if c == '(':
                d[i] = 0
            elif i > 0:
                if s[i - 1] == '(':
                    d[i] = max(d[i], d[i - 2] + 2)
                elif i - d[i - 1] - 1 >= 0 and s[i - d[i - 1] - 1] == '(':
                    if i - d[i - 1] - 2 >= 0:
                        d[i] = max(d[i], d[i - d[i - 1] - 2] + d[i - 1] + 2)
                    else:
                        d[i] = max(d[i], d[i - 1] + 2)
        return max(d) if d else 0


if __name__ == '__main__':
    f = Solution().longestValidParentheses
    assert f('()(()') == 2
    assert f(')(') == 0
    assert f('') == 0
    assert f('((') == 0
    assert f('(()') == 2
    assert f(')()())') == 4
