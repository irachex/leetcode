'''
https://leetcode.com/problems/find-the-duplicate-number/

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''


class Solution(object):
    def findDuplicate(self, nums):  # O(N). find loop in linked list
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    def findDuplicate_binary_search(self, nums):  # binary search, O(NlogN)
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        ans = 0
        left, right = 1, n
        while left <= right:
            mid = (left + right) / 2
            cnt = sum(1 for x in nums if x <= mid)
            if cnt > mid:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


if __name__ == '__main__':
    f = Solution().findDuplicate
    assert f([1, 2, 3, 4, 2]) == 2
    assert f([1, 2, 3, 4, 1]) == 1
    assert f([1, 2, 3, 4, 4]) == 4
    assert f([1, 2, 2, 4, 2]) == 2
