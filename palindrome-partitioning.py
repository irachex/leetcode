'''
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
'''

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        n = len(s)
        b = [[False for j in xrange(n)] for i in xrange(n)]
        q = []
        for i in xrange(n):
            b[i][i] = True
            q.append((i, i))
            if i > 0 and s[i] == s[i - 1]:
                b[i - 1][i] = True
                q.append((i - 1, i))

        while q:
            next_q = []
            for (i, j) in q:
                if i - 1 >= 0 and j + 1 < n and s[i - 1] == s[j + 1]:
                    b[i - 1][j + 1] = True
                    next_q.append((i - 1, j + 1))
            q = next_q

        d = [[] for i in xrange(n)]
        for i in xrange(n):
            if b[0][i]:
                d[i].append([s[:i + 1]])
            for j in xrange(1, i + 1):
                if b[j][i]:
                    d[i].extend((x + [s[j:i + 1]] for x in d[j - 1]))
        return d[n - 1]


if __name__ == '__main__':
    f = Solution().partition
    print f('aab')
