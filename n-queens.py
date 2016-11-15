#coding: utf-8

'''
http://oj.leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],
 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        if n == 0:
            return 0
        a = [0 for i in range(n)]
        result = []

        def solve(i, c=0, lt=0, rt=0):
            if i == n:
                sol = []
                for k in range(n):
                    row = ('Q' if j == a[k] else '.' for j in range(n))
                    sol.append(''.join(row))
                result.append(sol)
                return
            for j in range(n):
                if (not ((c >> j) & 1) and
                        not ((lt >> (i + j)) & 1) and
                        not ((rt >> (i - j + n)) & 1)):
                    a[i] = j
                    solve(i + 1,
                          c | (1 << j),
                          lt | (1 << (i + j)),
                          rt | (1 << (i - j + n)))

        solve(0)
        return result

if __name__ == "__main__":
    print Solution().solveNQueens(4)
