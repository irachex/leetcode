'''
https://leetcode.com/problems/island-perimeter/

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
'''


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0]) if grid else 0
        p = 0
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    s = 0
                    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        if 0 <= i + dx < n and 0 <= j + dy < m:
                            s += grid[i + dx][j + dy]
                    p += 4 - s
        return p


if __name__ == '__main__':
    f = Solution().islandPerimeter
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    assert f(grid) == 16
