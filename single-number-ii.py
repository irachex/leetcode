#coding: utf-8

'''
http://oj.leetcode.com/problems/single-number-ii/

Given an array of integers, every element appears three times except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = twos = thress = 0
        for x in A:
            twos |= ones & x
            ones ^= x
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones

    def singleNumber2(self, A):
        ans = 0
        sign = sum(1 for x in A if x < 0) % 3
        for i in range(33):
            s = 0
            for x in A:
                s += (abs(x) >> i) & 1
            ans |= (s % 3) << i
        if sign:
            ans = -ans
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.singleNumber([1, 1, 1, 2]) == 2
    assert s.singleNumber([1, 2, 3, 1, 2, 1, 2]) == 3
    assert s.singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]) == -4
