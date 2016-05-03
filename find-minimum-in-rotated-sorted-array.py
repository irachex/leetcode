'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] <= nums[-1]:  # not rotated
            return nums[0]

        ans = nums[0]
        left, right = 1, n - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                ans = min(ans, nums[mid])
                right = mid - 1
        return ans


if __name__ == '__main__':
    f = Solution().findMin
    assert f([4, 5, 6, 7, 0, 1, 2]) == 0
    assert f([4, 5]) == 4
    assert f([5, 4]) == 4
