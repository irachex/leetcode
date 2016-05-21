'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = ans = 0
        used = {}
        for j in xrange(n):
            if s[j] in used and i <= used[s[j]]:
                i = used[s[j]] + 1
            else:
                ans = max(ans, j - i + 1)
            used[s[j]] = j
        return ans


if __name__ == '__main__':
    f = Solution().lengthOfLongestSubstring
    assert f("abcabcbb") == 3
    assert f('bbbbb') == 1
    assert f('pwwkek') == 3
    assert f('') == 0
