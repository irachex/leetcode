#coding: utf-8

'''
http://oj.leetcode.com/problems/first-missing-positive/

Given an unsorted integer array, find the first missing positive integer.
For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A:
            return 1
        n = len(A)
        for i, x in enumerate(A):
            while x > 0 and x <= n and x != A[x - 1]:
                tmp = A[x - 1]
                A[x - 1] = x
                x = tmp

        for i in range(n):
            if A[i] != i + 1:
                return i + 1

        return n + 1


if __name__ == "__main__":
    s = Solution()
    assert s.firstMissingPositive([1]) == 2
    assert s.firstMissingPositive([1, 2, 0]) == 3
    assert s.firstMissingPositive([3, 4, -1, 1]) == 2
    assert s.firstMissingPositive([-1,4,2,1,9,10]) == 3
    assert s.firstMissingPositive([2, 1]) == 3
