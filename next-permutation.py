# coding: utf-8

'''
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(nums, x, y):
            tmp = nums[x]
            nums[x] = nums[y]
            nums[y] = tmp

        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            swap(nums, i, j)

        x, y = i + 1, n - 1
        while x < y:
            swap(nums, x, y)
            x += 1
            y -= 1


if __name__ == '__main__':
    f = Solution().nextPermutation

    def verify(nums, expect):
        f(nums)
        assert nums == expect

    verify([1, 2, 3], [1, 3, 2])
    verify([3, 2, 1], [1, 2, 3])
    verify([1, 1, 5], [1, 5, 1])
