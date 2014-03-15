#coding: utf-8

'''
http://oj.leetcode.com/problems/sqrtx/

Implement int sqrt(int x).
Compute and return the square root of x.
'''

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return 0
        x = float(x)
        z = 1.0
        last = 0.0
        while abs(z - last) >= 1e-6:
            last = z
            z -= (z * z - x) / (2.0 * z)
        return int(z)


if __name__ == "__main__":
    s = Solution()
    assert s.sqrt(4) == 2
    assert s.sqrt(9) == 3
    assert s.sqrt(16) == 4
