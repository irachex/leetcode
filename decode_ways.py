#coding: utf-8

'''
http://oj.leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
For example,
Given encoded message "12",
it could be decoded as "AB" (1 2) or "L" (12).
The number of ways decoding "12" is 2.
'''

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s:
            return 0
        n = len(s)
        d = [0 for i in range(n + 1)]
        d[0] = 1
        for i in range(1, n + 1):
            d[i] = 0
            if s[i - 1] != '0':
                d[i] += d[i - 1]
            if i >= 2 and int(s[i - 2:i]) <= 26 and s[i - 2] != '0':
                d[i] += d[i - 2]
        return d[n]


if __name__ == "__main__":
    s = Solution()
    # assert s.numDecodings('12') == 2
    # assert s.numDecodings('0') == 0
    assert s.numDecodings('10') == 1
