# coding: utf-8

'''
https://leetcode.com/problems/wildcard-matching/

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''


class Solution(object):

    def isMatch(self, s, p):  # Greedy O(N + M)
        n, m = len(s), len(p)
        i, j, before_star, star = 0, 0, None, None
        while i < n:
            if j < m and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
            elif j < m and p[j] == '*':
                star = j
                before_star = i
                j += 1
            elif star is not None:
                j = star + 1
                i = before_star + 1
                before_star += 1
            else:
                return False
        while j < m and p[j] == '*':
            j += 1
        return j == m

    def isMatch_DP(self, s, p):  # DP O(NM)
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) - p.count('*') > len(s):
            return False
        prev = [j == 0 for j in range(len(s) + 1)]
        for i in range(1, len(p) + 1):
            pc = p[i - 1]
            current = [False for j in range(len(s) + 1)]
            for j in range(0, len(s) + 1):
                if pc == '*':
                    current[j] = prev[j] or (j > 0 and prev[j - 1]) or (j > 0 and current[j - 1])
                elif pc == '?' and j > 0:
                    current[j] = prev[j - 1]
                elif j > 0:
                    current[j] = prev[j - 1] and pc == s[j - 1]
            prev = current
        return prev[len(s)]


if __name__ == '__main__':
    s = Solution()
    isMatch = s.isMatch
    assert isMatch('ho', '**ho')
    assert isMatch('a', 'a*')
    assert isMatch('', '*')
    assert isMatch('', '')
    assert isMatch("abcd", "a*")
    assert isMatch("aa", "a") is False
    assert isMatch("aa", "aa") is True
    assert isMatch("aaa", "aa") is False
    assert isMatch("aa", "*") is True
    assert isMatch("aa", "a*") is True
    assert isMatch("ab", "?*") is True
    assert isMatch("aab", "c*a*b") is False
