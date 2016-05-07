'''
https://leetcode.com/problems/rotate-array/

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:
Could you do it in-place with O(1) extra space?
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self._reverse(nums, 0, n - k - 1)
        self._reverse(nums, n - k, n - 1)
        self._reverse(nums, 0, n - 1)

    def _reverse(self, nums, s, e):
        for i in xrange((e - s + 1) / 2):
            tmp = nums[s + i]
            nums[s + i] = nums[e - i]
            nums[e - i] = tmp


if __name__ == '__main__':
    f = Solution().rotate
    nums = [1, 2, 3, 4, 5, 6, 7]
    f(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [1, 2, 3, 4, 5, 6]
    f(nums, 11)
    assert nums == [2, 3, 4, 5, 6, 1]
