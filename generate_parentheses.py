#coding: utf-8

'''
http://oj.leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"
'''

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 0:
            return []
        result = []

        def generate(i, s, cnt):
            if i == n * 2:
                if cnt == 0:
                    result.append(s)
                return
            if cnt > 0: # right
                generate(i + 1, '%s)' % s, cnt - 1)
            if cnt < n: # left
                generate(i + 1, '%s(' % s, cnt + 1)

        generate(0, '', 0)
        return result


if __name__ == "__main__":
    print Solution().generateParenthesis(3)
