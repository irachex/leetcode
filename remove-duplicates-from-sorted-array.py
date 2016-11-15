#coding: utf-8

'''
http://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2], Your function should return length = 2, and A is now [1,2].
'''

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        cnt = 0
        n = len(A)
        for i in range(1, n):
            if A[i] == A[i - 1]:
                cnt += 1
            elif cnt and i - cnt >= 0:
                A[i - cnt] = A[i]
        return n - cnt


if __name__ == "__main__":
    s = Solution()
    A = [1, 1, 2]
    s.removeDuplicates(A)
    assert A == [1, 2]
