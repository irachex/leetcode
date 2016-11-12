'''
https://leetcode.com/problems/sum-of-two-integers/

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''

class Solution(object):

    def getSum(self, a, b):
        mask = 0xffffffff
        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = carry << 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a

    def getSum_recursive(self, a, b):  # won't work for negative number
        return self.getSum(a ^ b, (a & b) << 1) if b != 0 else a

    def getSum2(self, a, b):  # won't work for negative number
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        n = r = 0
        w = 1
        while a | b:
            if (a & 1) & (b & 1):
                if r:
                    n |= w
                r = 1
            elif (a & 1) | (b & 1):
                if r:
                    r = 1
                else:
                    n |= w
                    r = 0
            else:
                if r:
                    n |= w
                    r = 0
            w <<= 1
            a >>= 1
            b >>= 1
        if r:
            n |= w
        return n


if __name__ == '__main__':
    f = Solution().getSum
    print f(-1, 1)
    assert f(-1, 1) == 0
    assert f(2, 4) == 6
    assert f(76341, 19734) == 76341 + 19734
