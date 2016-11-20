'''
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for x in nums:
            if x != 0:
                nums[pos] = x
                pos += 1
        while pos < len(nums):
            nums[pos] = 0
            pos += 1


if __name__ == '__main__':
    f = Solution().moveZeroes
    A = []
    f([])
    assert A == []
    A = [0, 1, 0, 3, 12]
    f(A)
    assert A == [1, 3, 12, 0, 0]
