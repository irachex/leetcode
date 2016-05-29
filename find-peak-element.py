# coding: utf-8

'''
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Note:
Your solution should be in logarithmic complexity.
'''


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return right

    def findPeakElement_linear(self, nums):
        for i in xrange(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return i - 1
        return len(nums) - 1


if __name__ == '__main__':
    f = Solution().findPeakElement
    assert f([1, 2, 3, 1]) == 2
