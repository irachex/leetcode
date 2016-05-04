# coding: utf-8

'''
https://leetcode.com/problems/majority-element/

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        cnt = 1
        for i in xrange(1, len(nums)):
            if nums[i] == m:
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    m = nums[i]
                    cnt = 1
        return m


if __name__ == '__main__':
    f = Solution().majorityElement
    assert f([2, 1, 3, 1, 1]) == 1
    assert f([1, 1, 2, 4, 1, 1, 3]) == 1
    assert f([3, 1, 2, 4, 1, 1, 1]) == 1
    assert f([3, 1, 2, 4, 1, 1, 1, 1]) == 1
