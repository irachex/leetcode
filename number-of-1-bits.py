# coding: utf-8

'''
https://leetcode.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            if n & 1:
                ans += 1
            n >>= 1
        return ans


if __name__ == '__main__':
    f = Solution().hammingWeight
    assert f(11) == 3
