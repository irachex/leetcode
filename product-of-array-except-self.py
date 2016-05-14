'''
https://leetcode.com/problems/product-of-array-except-self/

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0 for i in xrange(n)]
        for i in xrange(n):
            result[i] = result[i - 1] * nums[i - 1] if i > 0 else 1
        m = 1
        for i in reversed(xrange(n)):
            if i < n - 1:
                result[i] *= m
            m = m * nums[i]
        return result


if __name__ == '__main__':
    f = Solution().productExceptSelf
    assert f([1,2,3,4]) == [24,12,8,6]
    assert f([]) == []
