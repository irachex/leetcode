'''
https://leetcode.com/problems/palindrome-partitioning-ii/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        p = [[False for j in xrange(n)] for i in xrange(n)]
        for i in xrange(n):
            p[i][i] = True
            if i > 0 and s[i - 1] == s[i]:
                p[i - 1][i] = True
        for L in xrange(3, n + 1):
            for i in xrange(n - L + 1):
                j = i + L - 1
                if p[i + 1][j - 1] and s[i] == s[j]:
                    p[i][j] = True

        d = [(0 if p[0][i] else n + 1) for i in xrange(n)]
        for i in xrange(n):
            for j in xrange(i):
                if p[j + 1][i]:
                    d[i] = min(d[i], d[j] + 1)
        return d[n - 1] if n else 0


if __name__ == '__main__':
    f = Solution().minCut
    assert f('') == 0
    assert f('aab') == 1
    assert f('acabbad') == 3
    assert f('abcdcba') == 0
    print f("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")
