'''
https://leetcode.com/problems/dungeon-game/

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)  -3   3
-5     -10   1
10      30  -5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
'''


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n = len(dungeon)
        m = len(dungeon[0]) if dungeon else 0
        INF = 1 << 31
        d = [[INF for j in xrange(m + 1)] for i in xrange(n + 1)]
        d[n][m - 1] = d[n - 1][m] = 1

        for i in reversed(xrange(n)):
            for j in reversed(xrange(m)):
                d[i][j] = max(min(d[i + 1][j], d[i][j + 1]) - dungeon[i][j], 1)
        return d[0][0]


if __name__ == '__main__':
    f = Solution().calculateMinimumHP
    m = [[-2, -3, 3],
         [-5, -10, 1],
         [10, 30, -5]]
    assert f(m) == 7
