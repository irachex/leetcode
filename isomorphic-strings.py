'''
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = {}
        dt = {}
        cnt = 0
        for i in xrange(len(s)):
            i1 = ds.get(s[i])
            i2 = dt.get(t[i])
            if i1 != i2:
                return False
            if not i1:
                cnt += 1
                ds[s[i]] = dt[t[i]] = cnt
        return True


if __name__ == '__main__':
    f = Solution().isIsomorphic
    assert f('egg', 'add')
    assert not f('foo', 'bar')
    assert f('paper', 'title')
