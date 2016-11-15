#coding: utf-8

'''
http://oj.leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
Your algorithm should run in O(n) complexity.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        f = {}

        def find_root(x):
            if f[x] == x:
                return x
            f[x] = find_root(f[x])
            return f[x]

        for x in num:
            f[x] = x
            if x - 1 in f:
                f[x] = find_root(x - 1)
            if x + 1 in f:
                f[find_root(x + 1)] = f[x]

        ans = 0
        for x, parent in f.iteritems():
            ans = max(ans, x - find_root(parent) + 1)
        return ans


if __name__ == "__main__":
    print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
