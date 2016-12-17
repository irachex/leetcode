'''
https://leetcode.com/problems/shortest-palindrome/

Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:
Given "aacecaaa", return "aaacecaaa".
Given "abcd", return "dcbabcd".
'''


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def gen_next(p):
            m = len(p)
            next = [-1 for i in xrange(m)]
            next[0] = -1
            j = -1
            for i in xrange(1, m):
                while j != -1 and p[i] != p[j + 1]:
                    j = next[j]
                if p[i] == p[j + 1]:
                    j += 1
                next[i] = j
            return next

        p = s + '#' + s[::-1]
        next = gen_next(p)  # kmp
        n = len(s)
        add = n - next[n * 2] - 1  # 0..next[n * 2 + 1 - 1] + 1 is the longest prefix that s[:next[n * 2 + 1 - 1] + 1] is palindrome
        return s[n - add:][::-1] + s


if __name__ == '__main__':
    f = Solution().shortestPalindrome
    assert f('aacecaaa') == 'aaacecaaa'
    assert f('abcd') == 'dcbabcd'
    assert f('aaaa') == 'aaaa'
    assert f('') == ''
