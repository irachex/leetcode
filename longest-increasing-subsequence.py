'''
https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''

import sys

class Solution(object):

    def lengthOfLIS(self, nums):  # O(NlogN)
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        INF = sys.maxint
        f = [INF for i in xrange(n)]
        for i, ai in enumerate(nums):
            left, right = 0, i + 1
            pos = left
            while left <= right:
                mid = (left + right) >> 1
                if f[mid] >= ai:
                    right = mid - 1
                    pos = mid
                else:
                    left = mid + 1
            f[pos] = ai
        ans = 0
        while ans < n and f[ans] < INF:
            ans += 1
        return ans

    def lengthOfLIS_DP(self, nums):  # O(N^2)
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        d = [1 for i in xrange(n)]
        for i in xrange(1, n):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    d[i] = max(d[i], d[j] + 1)
        return max(d)


if __name__ == '__main__':
    f = Solution().lengthOfLIS
    assert f([10, 9, 2, 5, 3, 7, 101, 18]) == 4
