'''
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        ans = 1
        d = [[0 for j in xrange(m)] for i in xrange(n)]
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j):
            if d[i][j] != 0:
                return d[i][j]
            max_dist = 1
            for dx, dy in delta:
                x = i + dx
                y = j + dy
                if x >= 0 and x < n and y >= 0 and y < m and matrix[x][y] > matrix[i][j]:
                    max_dist = max(max_dist, dfs(x, y) + 1)
            d[i][j] = max_dist
            return max_dist

        for i in xrange(n):
            for j in xrange(m):
                ans = max(ans, dfs(i, j))
        return ans


if __name__ == '__main__':
    f = Solution().longestIncreasingPath
    matrix = [
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ]
    assert f(matrix) == 4

    matrix = [
        [3,4,5],
        [3,2,6],
        [2,2,1]
    ]
    assert f(matrix) == 4
