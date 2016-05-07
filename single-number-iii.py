'''
https://leetcode.com/problems/single-number-iii/

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a_xor_b = 0
        for x in nums:
            a_xor_b ^= x

        diff_bit = 1
        while True:
            if a_xor_b & diff_bit:
                break
            diff_bit <<= 1

        a = b = 0
        for x in nums:
            if x & diff_bit:
                a ^= x
            else:
                b ^= x
        return [a, b]


if __name__ == '__main__':
    f = Solution().singleNumber
    assert f([1, 2, 1, 3, 2, 5]) == [3, 5]
