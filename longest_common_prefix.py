#coding: utf-8

'''
http://oj.leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
'''


class Trie:

    def __init__(self):
        self.children = {}
        self.cnt = 0

    def add(self, s):
        node = self
        for c in s:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
            node.cnt += 1


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0:
            return ''
        trie = Trie()
        for i, s in enumerate(strs):
            trie.add(s)

        def dfs(node):
            m = 0
            s = ''
            for c, p in node.children.iteritems():
                if p.cnt == n:
                    cm, cs = dfs(p)
                    if m < cm + 1:
                        m = cm + 1
                        s = c + cs
            return m, s

        _, s = dfs(trie)
        return s


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(['ca', 'a']) == ''
    assert s.longestCommonPrefix(['ab', 'a']) == 'a'
    assert s.longestCommonPrefix(['aac', 'aac']) == 'aac'
