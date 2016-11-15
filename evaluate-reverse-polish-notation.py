#coding: utf-8

'''
http://oj.leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        def op(a, x, b):
            if x == '+':
                return a + b
            elif x == '-':
                return a - b
            elif x == '*':
                return a * b
            elif x == '/':
                # python hack
                # 6 / (-132) = -1 in python, should be 0
                return int(float(a) / b)

        stack = []
        for x in tokens:
            if x in ('+', '-', '*', '/'):
                a = stack.pop()
                b = stack.pop()
                c = op(b, x, a)
                stack.append(float(c))
            else:
                stack.append(float(x))
        return int(stack.pop())


if __name__ == "__main__":
    s = Solution()
    assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22

