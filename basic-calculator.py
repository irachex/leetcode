'''
https://leetcode.com/problems/basic-calculator/

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += '$'
        stack = [[1, 0]]  # [sign, value]
        sign, x = 1, 0
        for c in s:
            if c.isdigit():
                x = x * 10 + int(c)
            elif c == '+':
                stack[-1][1] += sign * x
                sign, x = 1, 0
            elif c == '-':
                stack[-1][1] += sign * x
                sign, x = -1, 0
            elif c == '(':
                stack.append([sign, 0])
                sign, x = 1, 0
            elif c == ')':
                stack[-1][1] += sign * x
                sign, x = 1, 0
                top_sign, top_value = stack.pop()
                stack[-1][1] += top_sign * top_value
            elif c == '$':
                stack[-1][1] += sign * x
        return stack[0][0] * stack[0][1]


if __name__ == '__main__':
    f = Solution().calculate
    assert f("1 + 1") == 2
    assert f(" 2-1 + 2 ") == 3
    assert f('(1+(4+5+2)-3)+(6+8)') == 23
    assert f('(1+(4+5+2)-3)-(6+8)') == (1+(4+5+2)-3)-(6+8)
