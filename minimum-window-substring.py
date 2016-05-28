'''
https://leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1
        n, m = len(s), len(t)
        min_w = n + 1
        i = j = cnt = start = 0
        while j < n:
            if d.get(s[j], -1) > 0:
                cnt += 1
            if s[j] in d:
                d[s[j]] -= 1
            if cnt == m:
                while i <= j and cnt == m:
                    if j - i + 1 < min_w:
                        min_w = j - i + 1
                        start = i
                    if d.get(s[i], -1) == 0:
                        cnt -= 1
                    if s[i] in d:
                        d[s[i]] += 1
                    i += 1
            j += 1

        return s[start:start + min_w] if min_w <= n else ''


if __name__ == '__main__':
    f = Solution().minWindow
    assert f('ADOBECODEBANC', 'ABC') == 'BANC'
