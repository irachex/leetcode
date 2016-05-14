# coding: utf-8

'''
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        def check(length):
            for i in xrange(length, n + 1):
                if ss[i] - ss[i - length] >= s:
                    return True
            return False

        n = len(nums)
        ss = [0 for i in xrange(n + 1)]
        for i in xrange(1, n + 1):
            ss[i] = ss[i - 1] + nums[i - 1]

        ans = 0
        left, right = 1, n
        while left <= right:
            mid = (left + right) / 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


if __name__ == '__main__':
    f = Solution().minSubArrayLen
    assert f(7, [2,3,1,2,4,3]) == 2
