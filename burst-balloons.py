# coding: utf-8
'''
https://leetcode.com/problems/burst-balloons/

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]
        d = [[0 for j in xrange(n + 2)] for i in xrange(n + 2)]
        for i in xrange(1, n + 1):
            d[i][i] = nums[i - 1] * nums[i] * nums[i + 1]
        for L in xrange(1, n + 1):
            for i in xrange(1, n - L + 2):
                j = i + L - 1
                for k in xrange(i, j + 1):
                    d[i][j] = max(d[i][j], d[i][k - 1] + d[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1])
        return d[1][n]

if __name__ == '__main__':
    f = Solution().maxCoins
    assert f([3, 1, 5, 8]) == 167
