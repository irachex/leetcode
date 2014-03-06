#coding: utf-8

'''
http://oj.leetcode.com/problems/powx-n/

Implement pow(x, n).
'''

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            x = 1.0 / x
            n = -n
        p = 1
        while n:
            if n & 1:
                p *= x
            n >>= 1
            x *= x
        return p


if __name__ == "__main__":
    s = Solution()
    assert s.pow(3, 3) == 27
    assert s.pow(2, 5) == 32
    assert s.pow(2, -1) == 0.5
