#coding: utf-8

'''
http://oj.leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays A and B, merge B into A as one sorted array.
Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
'''

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        a = b = 0
        C = []
        while True:
            if a < m and (b >= n or A[a] < B[b]):
                C.append(A[a])
                a += 1
            elif b < n and (a >= m or B[b] <= A[a]):
                C.append(B[b])
                b += 1
            else:
                break
        for i, x in enumerate(C):
            A[i] = x
        return A


if __name__ == "__main__":
    s = Solution()
    A = [1, 3, 5, 0, 0, 0]
    B = [2, 4, 6]
    assert s.merge(A, 3, B, 3) == [1, 2, 3, 4, 5, 6]
