'''
https://leetcode.com/problems/interleaving-string/

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n = len(s1)
        m = len(s2)
        if n + m != len(s3):
            return False
        d = [[False for j in xrange(m + 1)] for i in xrange(n + 1)]
        d[0][0] = True
        for i in xrange(n + 1):
            for j in xrange(m + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    d[i][j] = d[i][j] or d[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    d[i][j] = d[i][j] or d[i][j - 1]
        return d[n][m]


if __name__ == '__main__':
    f = Solution().isInterleave
    assert not f('a', '', 'c')
    assert f('aabcc', 'dbbca', 'aadbbcbcac')
    assert not f('aabcc', 'dbbca', 'aadbbbaccc')
