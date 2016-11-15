'''
https://leetcode.com/problems/distinct-subsequences/

Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''


class Solution(object):

    def numDistinct(self, s, t):
        # d[i][j] = sum{d[i - 1][k - 1] for k in [1,j] if s[i] == t[k]}
        # d[i][j] = d[i][j - 1] + d[i - 1][j - 1] if s[i] == t[j]

        n = len(t)
        m = len(s)
        d = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]
        d[0] = [1 for j in xrange(m + 1)]
        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                d[i][j] = d[i][j - 1]
                if t[i - 1] == s[j - 1]:
                    d[i][j] += d[i - 1][j - 1]
        return d[n][m]

    def numDistinct2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # d[i][j] = sum{d[i - 1][k - 1] for k in [1,j] if t[i] == s[k]}

        prev = [0 for i in xrange(len(s) + 1)]
        prev[0] = 1

        p = [[] for i in xrange(len(t) + 1)]
        p[0] = [0]
        for i in xrange(1, len(t) + 1):
            for j in xrange(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    p[i].append(j)

        for i in xrange(1, len(t) + 1):
            current = [0 for j in xrange(len(s) + 1)]
            ss = 0
            iter_prev = iter(p[i - 1])
            j_prev = next(iter_prev, None)
            for j in p[i]:
                while j_prev is not None and j_prev < j:
                    ss += prev[j_prev]
                    j_prev = next(iter_prev, None)
                current[j] = ss
            prev = current
        return sum(current)


if __name__ == '__main__':
    f = Solution().numDistinct
    assert f('eee', 'eee') == 1
    assert f('ddd', 'dd') == 3
    assert f('ccc', 'c') == 3
    assert f('rabbbit', 'rabbit') == 3
