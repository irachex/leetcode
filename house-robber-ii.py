'''
https://leetcode.com/problems/house-robber-ii/

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        d0 = [[0, 0] for i in range(n)]
        d1 = [[0, 0] for i in range(n)]
        d1[0] = [0, nums[0]]
        for i in xrange(1, n):
            d0[i][0] = max(d0[i - 1][0], d0[i - 1][1])
            d0[i][1] = d0[i - 1][0] + nums[i]

            d1[i][0] = max(d1[i - 1][0], d1[i - 1][1])
            d1[i][1] = d1[i - 1][0] + nums[i]
        return max(d0[n - 1][1], d1[n - 1][0])


if __name__ == '__main__':
    f = Solution().rob
    assert f([1]) == 1
    assert f([2, 1, 1, 2]) == 3
