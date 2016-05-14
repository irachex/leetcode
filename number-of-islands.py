'''
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(x, y, mark):
            d[x][y] = mark
            for t in xrange(4):
                p = x + dx[t]
                q = y + dy[t]
                if (p >= 0 and p < n and q >= 0 and q < m and
                        grid[p][q] == '1' and d[p][q] == 0):
                    dfs(p, q, mark)

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        n, m = len(grid), len(grid[0]) if grid else 0
        d = [[0 for j in xrange(m)] for i in xrange(n)]
        ans = 0
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == '1' and d[i][j] == 0:
                    ans += 1
                    dfs(i, j, ans)
        return ans


if __name__ == '__main__':
    f = Solution().numIslands
    x = [
        '11000',
        '11000',
        '00100',
        '00011',
    ]
    assert f(x) == 3
