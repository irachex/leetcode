'''
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''

class Solution(object):

    def longestSubstring(self, s, k):  # O(NlogN)
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def work(start, end):
            if end - start < k:
                return 0
            d = [0 for j in xrange(26)]
            for j in xrange(start, end):
                d[ord(s[j]) - 97] += 1
            for j in xrange(start, end):
                if d[ord(s[j]) - 97] < k:
                    return max(work(start, j), work(j + 1, end))
            return end - start

        return work(0, len(s))

    def longestSubstring_O_N(self, s, k):  # O(26N)
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        d = [None for i in xrange(n + 1)]
        p = [None for i in xrange(n + 1)]
        d[0] = [0 for j in xrange(26)]
        p[0] = [None for j in xrange(26)]
        for i, c in enumerate(s, start=1):
            d[i] = d[i - 1][:]
            d[i][ord(c) - 97] += 1
            p[i] = p[i - 1][:]
            p[i][ord(c) - 97] = i

        def work(start, end):
            if end - start + 1 < k:
                return 0
            for j in xrange(26):
                x = d[end][j] - d[start - 1][j]
                if 0 < x < k:
                    pos = p[end][j]
                    return max(work(start, pos - 1), work(pos + 1, end))
            return end - start + 1

        return work(1, n)


if __name__ == '__main__':
    f = Solution().longestSubstring
    assert f('ababc', 2) == 4
    assert f('aaabb', 3) == 3
    assert f('ababbc', 2) == 5
    assert f("ababacb", 3) == 0
