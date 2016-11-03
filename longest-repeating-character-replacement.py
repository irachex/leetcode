'''
https://leetcode.com/problems/longest-repeating-character-replacement/

Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        ans = 0
        for letter in set(s):
            start = replace = 0
            for i in xrange(n):
                if s[i] != letter:
                    replace += 1
                    if replace > k:
                        while start < n and s[start] == letter:
                            start += 1
                        if start < n:
                            start += 1
                            replace -= 1
                ans = max(ans, i - start + 1)
        return ans


if __name__ == '__main__':
    f = Solution().characterReplacement
    assert f("ABBB", 2) == 4
    assert f("ABAB", 2) == 4
    assert f("AABABBA", 1) == 4
