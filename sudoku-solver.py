#coding: utf-8

'''
http://oj.leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.
You may assume that there will be only one unique solution.
A sudoku puzzle...
...and its solution numbers marked in red.
'''

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):

        def get_square(x, y):
            return int(x / 3) * 3 + int(y / 3)

        a = [[int(c) if c != '.' else 0 for c in row] for row in board]

        bx = [[False for j in range(10)] for i in range(9)]
        by = [[False for j in range(10)] for i in range(9)]
        bs = [[False for j in range(10)] for i in range(9)]

        pos = []
        for i in range(9):
            for j in range(9):
                if a[i][j] == 0:
                    pos.append((i, j))
                else:
                    bx[i][a[i][j]] = True
                    by[j][a[i][j]] = True
                    bs[get_square(i, j)][a[i][j]] = True

        def dfs(dep):
            if dep == len(pos):
                return True
            for i in range(1, 10):
                x = pos[dep][0]
                y = pos[dep][1]
                s = get_square(x, y)
                if not bx[x][i] and not by[y][i] and not bs[s][i]:
                    bx[x][i] = by[y][i] = bs[s][i] = True
                    a[x][y] = i
                    if dfs(dep + 1):
                        return True
                    bx[x][i] = by[y][i] = bs[s][i] = False
            return False

        if dfs(0):
            for i in range(9):
                board[i] = ''.join(map(str, a[i]))


if __name__ == "__main__":
    pass
