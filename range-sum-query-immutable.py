# coding: utf-8

'''
https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
1. You may assume that the array does not change.
2. There are many calls to sumRange function.
'''

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self._s = [0]
        for i in xrange(1, len(nums) + 1):
            self._s.append(self._s[i - 1] + nums[i - 1])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._s[j + 1] - self._s[i]


if __name__ == '__main__':
    a = NumArray([-2, 0, 3, -5, 2, -1])
    assert a.sumRange(0, 2) == 1
    assert a.sumRange(2, 5) == -1
    assert a.sumRange(0, 5) == -3
