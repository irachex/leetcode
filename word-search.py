'''
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        n = len(board)
        m = len(board[0])
        b = [[False for j in range(m)] for i in range(n)]
        wlen = len(word)

        def dfs(x, y, dep):
            if dep == wlen:
                return True
            b[x][y] = True

            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if not (nx >= 0 and nx < n and ny >= 0 and ny < m):
                    continue
                if b[nx][ny]:
                    continue

                c = board[nx][ny]
                if c == word[dep]:
                    if dfs(nx, ny, dep + 1):
                        return True
            b[x][y] = False
            return False

        for i in range(n):
            for j in range(m):
                if word[0] == board[i][j]:
                    if dfs(i, j, 1):
                        return True
        return False


if __name__ == '__main__':
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    f = Solution().exist
    assert f(board, 'ABCCED')
    assert f(board, 'SEE')
    assert f(board, 'ABCB') is False
