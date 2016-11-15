'''
https://leetcode.com/problems/word-search-ii/

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
'''


class TrieNode(object):

    def __init__(self, value=None):
        self.edges = {}
        self.value = value


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, value):
        p = self.root
        for c in s:
            node = p.edges.get(c)
            if node is None:
                node = TrieNode()
                p.edges[c] = node
            p = node
        p.value = value


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        trie = Trie()
        for i, s in enumerate(words):
            trie.insert(s, i)

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        n = len(board)
        m = len(board[0])
        b = [[False for j in range(m)] for i in range(n)]
        f = [False for i in range(len(words))]

        def dfs(x, y, p):
            b[x][y] = True
            if p.value is not None:
                f[p.value] = True
            if not p.edges:
                b[x][y] = False
                return

            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if not (nx >= 0 and nx < n and ny >= 0 and ny < m):
                    continue
                if b[nx][ny]:
                    continue

                c = board[nx][ny]
                node = p.edges.get(c)
                if node:
                    dfs(nx, ny, node)
            b[x][y] = False

        for i in range(n):
            for j in range(m):
                node = trie.root.edges.get(board[i][j])
                if node:
                    dfs(i, j, node)

        return [s for i, s in enumerate(words) if f[i]]


if __name__ == '__main__':
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    f = Solution().findWords
    # print f(board, words)

    print f(["ab","aa"], ["aba","baa","bab","aaab","aaa","aaaa","aaba"])
