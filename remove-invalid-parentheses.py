'''
https://leetcode.com/problems/remove-invalid-parentheses/

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
'''


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if not n:
            return [s]
        d = [[(0 if i > j else n + 1) for j in xrange(n)] for i in xrange(n)]
        p = [[set(['']) for j in xrange(n)] for i in xrange(n)]

        def update(i, j, value, result):
            if d[i][j] > value:
                d[i][j] = value
                p[i][j] = set(result)
            elif d[i][j] == value:
                p[i][j] = p[i][j].union(result)

        for i in xrange(n):
            if s[i] in '()':
                d[i][i] = 1
                p[i][i] = set([''])
            else:
                d[i][i] = 0
                p[i][i] = set(s[i])

        for L in xrange(2, n + 1):
            for i in xrange(n - L + 1):
                j = i + L - 1
                if s[i] == '(' and s[j] == ')':
                    r = ('(%s)' % x for x in p[i + 1][j - 1])
                    update(i, j, d[i + 1][j - 1], r)
                for k in xrange(i, j):
                    r = (x + y for x in p[i][k] for y in p[k + 1][j])
                    update(i, j, d[i][k] + d[k + 1][j], r)
        return list(p[0][n - 1])


if __name__ == '__main__':
    f = Solution().removeInvalidParentheses
    print f('n')
    print f('(')
    print f('')
    print f("(a)())()")
    print f("()())()")
    print f(")(")
    print f('((())')
    print f('))(((((()())(()')
