'''
https://leetcode.com/problems/reverse-bits/

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
'''

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        for i in range(32):
            x = x << 1
            if n & 1:
                x += 1
            n >>= 1
        return x

    def reverseBits_bit(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


if __name__ == '__main__':
    f = Solution().reverseBits
    assert f(43261596) == 964176192
