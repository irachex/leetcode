#coding: utf-8

'''
http://oj.leetcode.com/problems/n-queens-ii/

Follow up for N-Queens problem.
Now, instead outputting board configurations, return the total number of distinct solutions.
'''

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        if n == 0:
            return 0
        result = [0]

        def solve(i, c=0, lt=0, rt=0):
            if i == n:
                result[0] += 1
                return
            for j in range(n):
                if (not ((c >> j) & 1) and
                        not ((lt >> (i + j)) & 1) and
                        not ((rt >> (i - j + n)) & 1)):
                    solve(i + 1,
                          c | (1 << j),
                          lt | (1 << (i + j)),
                          rt | (1 << (i - j + n)))

        solve(0)
        return result[0]
