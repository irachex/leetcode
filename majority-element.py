# coding: utf-8

'''
https://leetcode.com/problems/majority-element/

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution(object):
    def majorityElement(self, nums):  # Boyer-Moore Majority Vote Algorithm
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = count = 0
        for x in nums:
            if count == 0:
                candidate = x
            if candidate == x:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == '__main__':
    f = Solution().majorityElement
    assert f([2, 1, 3, 1, 1]) == 1
    assert f([1, 1, 2, 4, 1, 1, 3]) == 1
    assert f([3, 1, 2, 4, 1, 1, 1]) == 1
    assert f([3, 1, 2, 4, 1, 1, 1, 1]) == 1
