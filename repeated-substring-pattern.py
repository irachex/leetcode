'''
https://leetcode.com/problems/repeated-substring-pattern/

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type str: s
        :rtype: bool
        """
        n = len(s)
        for k in xrange(1, n / 2 + 1):
            if s[k] == s[0] and s[k - 1] == s[-1] and n % k == 0:
                flag = True
                for i in xrange(1, n / k):
                    if not all(s[i * k + j] == s[j] for j in xrange(k)):
                        flag = False
                        break
                if flag:
                    return True
        return False

    def repeatedSubstringPattern_KMP(self, s):
        """
        :type str: s
        :rtype: bool
        """

        def gen_next(p):
            n = len(p)
            # next[i] = j if exist j such that p[0..j] == p[i-j..i] else -1
            next = [0 for i in xrange(n)]
            next[0] = -1
            j = -1
            for i in xrange(1, n):
                while j >= 0 and p[i] != p[j + 1]:
                    j = next[j]
                if p[i] == p[j + 1]:
                    j += 1
                next[i] = j
            return next

        n = len(s)
        next = gen_next(s)
        L = next[n - 1] + 1
        return next[n - 1] != -1 and n % (n - L) == 0


if __name__ == '__main__':
    f = Solution().repeatedSubstringPattern_KMP
    assert not f("ababac")
    assert f('abab')
    assert not f('aba')
    assert f('abcabcabcabc')
    assert f('abacabac')
    assert f('abcadabcad')
