# coding: utf-8

'''
http://oj.leetcode.com/problems/maximum-subarray/

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

More practice:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        """
        O(n)
        """
        INF = 999999999
        s = 0
        ans = -INF
        for x in A:
            s += x
            ans = max(ans, s)
            if s < 0:
                s = 0
        return ans

    def maxSubArray2(self, A):
        """
        O(nlogn) using the divide and conquer approach
        """
        if len(A) == 0:
            return 0
        return self.maxSubArray2Helper(A, 0, len(A) - 1)

    def maxSubArray2Helper(self, A, left, right):
        if left == right:
            return A[left]
        mid = (left + right) / 2
        left_ans = self.maxSubArray2Helper(A, left, mid)
        right_ans = self.maxSubArray2Helper(A, mid + 1, right)

        left_max = A[mid]
        right_max = A[mid + 1]
        tmp = 0
        for i in range(mid, left - 1, -1):
            tmp += A[i]
            if left_max < tmp:
                left_max = tmp
        tmp = 0
        for i in range(mid + 1, right + 1):
            tmp += A[i]
            if right_max < tmp:
                right_max = tmp
        return max(left_ans, right_ans, left_max + right_max)


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([-1]) == -1
