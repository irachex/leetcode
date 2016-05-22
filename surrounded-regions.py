'''
https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0]) if board else 0
        b = [[False for j in xrange(m)] for i in xrange(n)]

        def dfs(i, j):
            b[i][j] = True
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                x = i + dx
                y = j + dy
                if x > 0 and x < n and y > 0 and y < m:
                    if not b[x][y] and board[x][y] == 'O':
                        dfs(x, y)

        for i in xrange(n):
            for j in (0, m - 1):
                if not b[i][j] and board[i][j] == 'O':
                    dfs(i, j)
        for i in (0, n - 1):
            for j in xrange(m):
                if not b[i][j] and board[i][j] == 'O':
                    dfs(i, j)
        for i in xrange(n):
            for j in xrange(m):
                if not b[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == '__main__':
    f = Solution().solve
    board = ['X X X X'.split(),
             'X O O X'.split(),
             'X X O X'.split(),
             'X O X X'.split()]
    f(board)
    print board
