# coding: utf-8

'''
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
'''

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_steps(a, b):
            steps = 0
            while a <= n:
                steps += b - a if b <= n else n - a + 1
                a *= 10
                b *= 10
            return steps

        curr = 1
        k -= 1
        while k > 0:
            steps = count_steps(curr, curr + 1)  # nodes between curr and curr + 1
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10  # next layer
                k -= 1
        return curr


if __name__ == '__main__':
    def g(n, k):
        return int(list(sorted(map(str, xrange(1, n + 1))))[k - 1])

    f = Solution().findKthNumber
    assert f(100, 10) == g(100, 10)
    assert f(13, 2) == 10
    assert f(13, 1) == 1
    assert f(13, 5) == 13
    assert f(13, 6) == 2
    assert f(13, 7) == 3
    assert f(2132, 183) == g(2132, 183)
