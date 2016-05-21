# coding: utf-8

'''
https://leetcode.com/problems/increasing-triplet-subsequence/

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        INF = 1 << 31
        min1 = min2 = INF
        for x in nums:
            if x <= min1:
                min1 = x
            elif x <= min2:
                min2 = x
            else:
                return True
        return False


if __name__ == '__main__':
    f = Solution().increasingTriplet
    assert f([1, 2, 3, 4, 5])
    assert not f([5, 4, 3, 2, 1])
    assert not f([1, 1, 1, 1, 1])
    assert not f([1, 2, 2, 1])
