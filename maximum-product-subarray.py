'''
https://leetcode.com/problems/maximum-product-subarray/

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_p = min_p = ans = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] >= 0:
                max_p = max(nums[i], max_p * nums[i])
                min_p = min(nums[i], min_p * nums[i])
            else:
                tmp = max_p
                max_p = max(nums[i], min_p * nums[i])
                min_p = min(nums[i], tmp * nums[i])
            ans = max(ans, max_p)
        return ans


if __name__ == '__main__':
    f = Solution().maxProduct
    assert f([-4,-3,-2]) == 12
    assert f([2,3,-2,4]) == 6
