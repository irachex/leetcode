#coding: utf-8

'''
http://oj.leetcode.com/problems/word-break/

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
For example, givens = "leetcode",dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code".
'''

class Solution:
    # @param s, a string
    # @param words, a set of string
    # @return a boolean
    def wordBreak(self, s, words):
        if not words:
            return False
        n = len(s)
        d = [False for i in range(n + 1)]
        d[0] = True
        for i in range(1, n + 1):
            for j, w in enumerate(words):
                if i >= len(w) and d[i - len(w)] and w == s[i - len(w):i]:
                    d[i] = True
                    break
        return d[n]


if __name__ == "__main__":
    s = Solution()
    assert s.wordBreak("leetcode", ['leet', 'code'])
    assert not s.wordBreak("a", ['b'])
