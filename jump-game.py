#coding: utf-8

'''
http://oj.leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
'''

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if not A:
            return False
        n = len(A)
        can_reach = 0
        i = 0
        while i < n and i <= can_reach:
            if i + A[i] >= can_reach:
                can_reach = i + A[i]
            if can_reach >= n - 1:
                return True
            i += 1
        return can_reach >= n - 1


if __name__ == "__main__":
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4]) is True
    assert s.canJump([3, 2, 1, 0, 4]) is False
    assert s.canJump([1, 2]) is True
