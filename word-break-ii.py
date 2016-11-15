#coding: utf-8

'''
http://oj.leetcode.com/problems/word-break-ii/

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.
For example, givens = "catsanddog",dict = ["cat", "cats", "and", "sand", "dog"].
A solution is ["cats and dog", "cat sand dog"].
'''

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, words):
        if not words:
            return []
        words = list(words)
        n = len(s)
        d = [False for i in range(n + 1)]
        p = [[] for i in range(n + 1)]
        d[0] = True
        for i in range(1, n + 1):
            for j, w in enumerate(words):
                if i >= len(w) and d[i - len(w)] and w == s[i - len(w):i]:
                    d[i] = True
                    p[i].append(j)

        result = []
        a = [None for i in range(n + 1)]

        def dfs(i, dep):
            if i == 0:
                result.append(' '.join(words[a[j]] for j in range(dep - 1, -1, -1)))
                return
            for j in p[i]:
                a[dep] = j
                dfs(i - len(words[j]), dep + 1)

        dfs(n, 0)

        return result


if __name__ == "__main__":
    s = Solution()
    print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
