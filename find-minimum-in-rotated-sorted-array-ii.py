'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''


class Solution(object):
    def findMin(self, nums):  # worst case O(N)
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]


if __name__ == '__main__':
    f = Solution().findMin
    assert f([10, 1, 10, 10, 10]) == 1
    assert f([3, 1]) == 1
    assert f([4, 5, 6, 7, 0, 1, 2]) == 0
    assert f([4, 5, 6, 7, 0, 1, 2, 4]) == 0
    assert f([4, 4, 4, 5, 4, 4]) == 4
    assert f([0]) == 0
