'''
https://leetcode.com/problems/power-of-two/

Given an integer, write a function to determine if it is a power of two.
'''

class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n == (n & -n)

    def isPowerOfTwo_bit(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if n & 1:
                return False
            n >>= 1
        return n == 1

if __name__ == '__main__':
    f = Solution().isPowerOfTwo
    assert not f(3)
    assert f(536870912)
    assert not f(2097153)
