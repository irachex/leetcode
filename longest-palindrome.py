'''
https://leetcode.com/problems/longest-palindrome/

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        r = 0
        odd = False
        for k, v in d.iteritems():
            if v & 1:
                odd = True
                r += v - 1
            else:
                r += v
        if odd:
            r += 1
        return r


if __name__ == '__main__':
    f = Solution().longestPalindrome
    assert f('abccccdd') == 7
