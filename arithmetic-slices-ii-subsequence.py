# coding: utf-8

'''
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0 < P1 < ... < Pk < N.
A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k ≥ 2.
The function should return the number of arithmetic subsequence slices in the array A.
The input contains N integers. Every integer is in the range of -231 and 231-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 231-1.


Example:
Input: [2, 4, 6, 8, 10]
Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
'''


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        ans = 0
        d = [{} for i in xrange(n)]  # d[i][k] is num of seqs ends with A[i] and diff is k, including length 2
        for i in xrange(n):
            for j in xrange(i + 1, n):
                k = A[j] - A[i]
                d[j][k] = d[j].get(k, 0) + 1  # add one seq that length is 2
                if d[i].get(k):
                    d[j][k] += d[i][k]
                    ans += d[i][k]  # d[j][k] is including length 2, d[i][k] is what we sum up.
        return ans


if __name__ == '__main__':
    f = Solution().numberOfArithmeticSlices
    assert f([2, 2, 3, 4]) == 2
    assert f([2, 4, 6, 8, 10]) == 7
    assert f([1, 3, 3, 5]) == 2
    assert f([1]) == 0
    assert f([1, 2, 3, 4, 5]) == 7
