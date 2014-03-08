#coding: utf-8

'''
http://oj.leetcode.com/problems/valid-sudoku/

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
A partially filled sudoku which is valid.
Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        def is_valid(s):
            c = [False for i in range(10)]
            for x in s:
                if x > 0 and c[x]:
                    return False
                c[x] = True
            return True

        a = [[0 for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                a[i][j] = int(board[i][j]) if board[i][j] != '.' else 0
        for i in range(9):
            if not is_valid(a[i]):
                return False
            if not is_valid([a[j][i] for j in range(9)]):
                return False
            if not is_valid([a[x][y] for x in range(i * 3 % 9, i * 3 % 9 + 3) for y in range(i / 3 * 3, i / 3 * 3 + 3)]):
                return False
        return True


if __name__ == "__main__":
    a = [".9..4....",
         "1.....6..",
         "..3......",
         ".........",
         "...7.....",
         "3...5....",
         "..7..4...",
         ".........",
         "....7...."]
    assert Solution().isValidSudoku(a)
