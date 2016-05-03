'''
https://leetcode.com/problems/combination-sum-iii/

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.

Example 1:
Input: k = 3, n = 7
Output: [[1, 2, 4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def range_sum(a, b):
            return (a + b) * (b - a + 1) / 2

        if range_sum(9 - k + 1, 9) < n:
            return []

        a = [0 for i in xrange(k)]
        result = []

        def dfs(i, last, s):
            if i == k - 1:
                a[k - 1] = n - s
                if a[k - 1] > last and a[k - 1] <= 9:
                    result.append(a[:])
                return

            for j in xrange(last + 1, min(n - range_sum(last + 2, last + k - i), 9) + 1):
                a[i] = j
                dfs(i + 1, j, s + j)

        dfs(0, 0, 0)
        return result


if __name__ == '__main__':
    f = Solution().combinationSum3
    assert f(2, 18) == []
    assert f(8, 36) == [[1, 2, 3, 4, 5, 6, 7, 8]]
    assert f(3, 7) == [[1, 2, 4]]
    assert f(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
