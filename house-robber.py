'''
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

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
        d = [[0, 0] for i in range(n)]
        d[0] = [0, nums[0]]
        for i in xrange(1, n):
            d[i][0] = max(d[i - 1][0], d[i - 1][1])
            d[i][1] = d[i - 1][0] + nums[i]
        return max(d[n - 1])


if __name__ == '__main__':
    f = Solution().rob
    assert f([2,1,1,2]) == 4
