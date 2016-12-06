'''
https://leetcode.com/problems/unique-substrings-in-wraparound-string/

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1
Explanation: Only the substring "a" of string "a" is in the string s.

Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.

Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
'''


class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        d = [0 for i in xrange(26)]
        start = 0
        for i, c in enumerate(p):
            x = ord(c) - 97
            if not (i > 0 and (ord(c) - ord(p[i - 1]) + 26) % 26 == 1):
                start = i
            d[x] = max(d[x], i - start + 1)
        return sum(d)


if __name__ == '__main__':
    f = Solution().findSubstringInWraproundString
    assert f('a') == 1
    assert f('cac') == 2
    assert f('zab') == 6
    assert f('zabcdefghijklmnopqrstuvwxyz') == 377
