#coding: utf-8

'''
http://oj.leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        if not s:
            return True
        stack = [None for x in s]
        top = -1
        REV = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for ch in s:
            if ch in ('(', '[', '{'):
                top += 1
                stack[top] = ch
            else:
                if not (top >= 0 and stack[top] == REV[ch]):
                    return False
                top -= 1
        return top == -1


if __name__ == "__main__":
    s = Solution()
    assert s.isValid('()')
    assert s.isValid('()[]{}')
    assert not s.isValid('(]')
    assert not s.isValid('([)]')
