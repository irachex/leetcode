'''
https://leetcode.com/problems/longest-palindromic-substring/

Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

class Solution(object):

    def longestPalindrome(self, s):
        # Manacher's algorithm http://articles.leetcode.com/longest-palindromic-substring-part-ii
        if not s:
            return ''
        t = '#'.join('^{}$'.format(s))
        n = len(t)
        p = [0 for i in xrange(n)]
        center = right = 0
        for i in xrange(1, n - 1):
            i_mirror = center * 2 - i  # center - i_mirror = i - center
            # if right - i > p[i_mirror] then p[i] = p[i_mirror] else p[i] >= right - i
            p[i] = min(right - i, p[i_mirror]) if right > i else 0
            while t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1

            if i + p[i] > right:
                center = i
                right = i + p[i]

        max_len = center = 0
        for i in xrange(n - 1):
            if max_len < p[i]:
                max_len = p[i]
                center = i
        return s[(center - max_len) / 2:(center + max_len) / 2]

    def longestPalindrome_bisection(self, s):  # bisection, O(N^2lgN) ACed
        """
        :type s: str
        :rtype: str
        """
        def check(L):
            for i in xrange(n - L + 1):
                e = i + L - 1
                for j in xrange(L / 2 + 1):
                    if s[i + j] != s[e - j]:
                        break
                else:
                    return True, i, i + L - 1
            return False, None, None

        n = len(s)
        left, right = 0, n
        ri = rj = 0
        while left <= right:
            mid = (left + right) / 2
            ok, i, j = check(mid)
            if ok:
                left = mid + 1
                ri, rj = i, j
            else:
                ok, i, j = check(mid + 1)
                if ok:
                    left = mid + 2
                    ri, rj = i, j
                else:
                    right = mid - 1
        return s[ri:rj + 1] if n else ''

    def longestPalindrome_DP(self, s):  # O(N^2)  TLE
        n = len(s)
        max_len = ri = rj = 0
        q = [(i, i) for i in xrange(n)]
        for i in xrange(n - 1):
            if s[i] == s[i + 1]:
                q.append((i, i + 1))
        while q:
            next_q = []
            for (i, j) in q:
                if max_len < j - i + 1:
                    max_len = j - i + 1
                    ri, rj = i, j
                if i - 1 >= 0 and j + 1 < n and s[i - 1] == s[j + 1]:
                    next_q.append((i - 1, j + 1))
            q = next_q
        return s[ri:rj + 1] if n else ''


if __name__ == '__main__':
    f = Solution().longestPalindrome
    assert f('abc01234567654321cbs') == '1234567654321'
