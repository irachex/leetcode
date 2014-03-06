#coding: utf-8

'''
http://oj.leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
For example,
If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        a = [0 for i in range(k)]
        result = []

        def generate(i, last):
            if i == k:
                result.append(a[:])
                return
            for j in range(last + 1, n + 1):
                a[i] = j
                generate(i + 1, j)

        generate(0, 0)

        return result


if __name__ == "__main__":
    print Solution().combine(4, 2)
