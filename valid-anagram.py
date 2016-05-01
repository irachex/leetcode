'''
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count_s = {}
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        return all(count_t.get(k) == v for k, v in count_s.iteritems())


if __name__ == '__main__':
    f = Solution().isAnagram
    assert f('anagram', 'nagaram')
    assert f('rat', 'car') is False
