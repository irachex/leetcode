'''
https://leetcode.com/problems/trapping-rain-water-ii/

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
'''


import heapq


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        n = len(heightMap)
        m = len(heightMap[0]) if heightMap else 0
        b = [[False for j in xrange(m)] for i in xrange(n)]
        q = []
        for i in xrange(n):
            b[i][0] = b[i][m - 1] = True
            heapq.heappush(q, (heightMap[i][0], i, 0))
            heapq.heappush(q, (heightMap[i][m - 1], i, m - 1))
        for j in xrange(m):
            b[0][j] = b[n - 1][j] = True
            heapq.heappush(q, (heightMap[0][j], 0, j))
            heapq.heappush(q, (heightMap[n - 1][j], n - 1, j))
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ans = 0
        while q:
            h, tx, ty = heapq.heappop(q)
            for dx, dy in dirs:
                x = tx + dx
                y = ty + dy
                if x >= 0 and x < n and y >= 0 and y < m and not b[x][y]:
                    b[x][y] = True
                    ans += max(0, h - heightMap[x][y])
                    heapq.heappush(q, (max(h, heightMap[x][y]), x, y))
        return ans


if __name__ == '__main__':
    f = Solution().trapRainWater
    assert f([
        [1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]
    ]) == 4
