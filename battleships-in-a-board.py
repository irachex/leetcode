'''
https://leetcode.com/problems/battleships-in-a-board/

Given an 2D board, count how many different battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is not a valid board - as battleships will always have a cell separating between them.

Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
'''


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        n = len(board)
        m = len(board[0]) if board else 0
        ans = 0
        for i in xrange(n):
            for j in xrange(m):
                if (board[i][j] == 'X' and
                        (i + 1 == n or board[i + 1][j] == '.') and
                        (j + 1 == m or board[i][j + 1] == '.')):
                    ans += 1
        return ans


if __name__ == '__main__':
    f = Solution().countBattleships
    assert f(["X..X","...X","...X"]) == 2
