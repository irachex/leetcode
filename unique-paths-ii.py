'''
https://leetcode.com/problems/unique-paths-ii/

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        d = [[0 for j in xrange(m)] for i in xrange(n)]
        for i in xrange(n):
            for j in xrange(m):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        d[i][j] = 1
                    elif i == 0:
                        d[i][j] = d[i][j - 1]
                    elif j == 0:
                        d[i][j] = d[i - 1][j]
                    else:
                        d[i][j] = d[i - 1][j] + d[i][j - 1]
                else:
                    d[i][j] = 0
        return d[n - 1][m - 1]


if __name__ == '__main__':
    f = Solution().uniquePathsWithObstacles
    grid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    assert f(grid) == 2
