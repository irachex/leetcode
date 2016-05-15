'''
https://leetcode.com/problems/game-of-life/

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0]) if board else 0

        t = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        for i in xrange(n):
            for j in xrange(m):
                live = 0
                for dx, dy in t:
                    x = i + dx
                    y = j + dy
                    if x >= 0 and x < n and y >= 0 and y < m and board[x][y] & 1:
                        live += 1
                curr = board[i][j] & 1
                next = 0
                if curr:
                    if live < 2:
                        next = 0
                    elif live == 2 or live == 3:
                        next = 1
                    elif live > 3:
                        next = 0
                else:
                    if live == 3:
                        next = 1
                board[i][j] |= next << 1

        for i in xrange(n):
            for j in xrange(m):
                board[i][j] >>= 1
