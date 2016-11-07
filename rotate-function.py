'''
https://leetcode.com/problems/rotate-function/

Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
'''


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        s = sum(A)
        f = sum(i * Ai for i, Ai in enumerate(A))
        ans = f
        for i in xrange(1, n):
            next_f = f + s - n * A[n - i]
            ans = max(ans, next_f)
            f = next_f
        return ans


# F[0]        = 0 * A[0] + 1 * A[1] + 2 * A[2] + 3 * A[3]
# F[1]        = 0 * A[3] + 1 * A[0] + 2 * A[1] + 3 * A[2]
# F[1] - F[0] = 0 * A[3] + 1 * A[0] + 2 * A[1] + 3 * A[2] - (0 * A[0] + 1 * A[1] + 2 * A[2] + 3 * A[3])
#             = 1 * A[0] + 1 * A[1] + 1 * A[2] - 3 * A[3]
# F[i] = 0 * A[n - i] + 1 * A[n - i + 1] + ... + i * A[0] + (i + 1) * A[1] + ... + n * A[n - i]
# F[i] - F[i - 1] = sum(A) - A[i] - (n - 1) * A[n - i] = sum(A) - n * A[n - i]


if __name__ == '__main__':
    f = Solution().maxRotateFunction
    assert f([4, 3, 2, 6]) == 26
