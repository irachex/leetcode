'''
https://leetcode.com/problems/basic-calculator-ii/

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
'''


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        x, op = 0, '+'
        for c in s + '$':
            if c.isdigit():
                x = x * 10 + int(c)
            elif c != ' ':
                if op == '+':
                    stack.append(x)
                elif op == '-':
                    stack.append(-x)
                elif op == '*':
                    stack.append(stack.pop() * x)
                elif op == '/':
                    last = stack.pop()
                    if last == 0:
                        stack.append(0)
                    else:
                        stack.append(abs(last) / x * last / abs(last))
                x, op = 0, c
        return sum(stack) if stack else 0


if __name__ == '__main__':
    f = Solution().calculate
    assert f('0/1') == 0
    assert f('14-3/2') == 13
    assert f('3+2*2') == 7
    assert f(' 3/2 ') == 1
    assert f(' 3+5 / 2 ') == 5
