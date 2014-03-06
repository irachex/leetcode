#coding: utf-8

'''
http://oj.leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
'''

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        d = [[x for x in row] for row in grid]
        m = len(grid)
        n = len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    d[i][j] = d[i][j - 1] + grid[i][j]
                elif j == 0:
                    d[i][j] = d[i - 1][j] + grid[i][j]
                else:
                    d[i][j] = min(d[i - 1][j], d[i][j - 1]) + grid[i][j]
        return d[m - 1][n - 1]


if __name__ == "__main__":
    assert Solution().minPathSum([[1, 2], [1, 1]]) == 3
