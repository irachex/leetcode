# coding: utf-8

'''
https://leetcode.com/problems/majority-element-ii/

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

Hint:

How many majority elements could it possibly have?
'''


class Solution(object):
    def majorityElement(self, nums):  # Boyer-Moore Majority Vote Algorithm
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candidate1 = candidate2 = None
        count1 = count2 = 0
        for x in nums:
            if x == candidate1:
                count1 += 1
            elif x == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = x, 1
            elif count2 == 0:
                candidate2, count2 = x, 1
            else:
                count1 -= 1
                count2 -= 1
        return [x for x in [candidate1, candidate2] if nums.count(x) > len(nums) / 3]


if __name__ == '__main__':
    f = Solution().majorityElement
    assert f([]) == []
    assert f([2, 2]) == [2]
    assert f([0, 0, 0]) == [0]
    assert f([3, 2, 1, 3, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
