'''
https://leetcode.com/problems/pacific-atlantic-water-flow/

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0]) if matrix else 0
        p = [[False for j in xrange(m)] for i in xrange(n)]
        a = [[False for j in xrange(m)] for i in xrange(n)]
        t = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(i, j, c):
            c[i][j] = True
            for dx, dy in t:
                x = i + dx
                y = j + dy
                if (x >= 0 and x < n and y >= 0 and y < m and
                        matrix[i][j] <= matrix[x][y] and not c[x][y]):
                    dfs(x, y, c)

        for i in xrange(n):
            dfs(i, 0, p)
            dfs(i, m - 1, a)
        for j in xrange(m):
            dfs(0, j, p)
            dfs(n - 1, j, a)

        result = []
        for i in xrange(n):
            for j in xrange(m):
                if p[i][j] and a[i][j]:
                    result.append([i, j])
        return result


if __name__ == '__main__':
    f = Solution().pacificAtlantic
    assert f([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
