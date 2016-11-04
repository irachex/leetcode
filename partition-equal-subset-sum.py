'''
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        s = sum(nums)
        if s & 1:
            return False
        d = [False for i in xrange(s / 2 + 1)]
        d[0] = True
        for x in nums:
            for i in reversed(xrange(x, s / 2 + 1)):
                d[i] = d[i] or d[i - x]
        return d[s / 2]


if __name__ == '__main__':
    f = Solution().canPartition
    assert f([1, 5, 11, 5])
    assert not f([1, 2, 3, 5])
