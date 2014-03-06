#coding: utf-8

'''
http://oj.leetcode.com/problems/subsets/

Given a set of distinct integers, S, return all possible subsets.\nNote:Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.\nFor example,
If S = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        n = len(S)
        a = [0 for i in range(n)]
        result = []

        def generate(i, last):
            result.append(a[:i])
            if i == n:
                return
            for j in range(last + 1, n):
                a[i] = S[j]
                generate(i + 1, j)

        generate(0, -1)

        return result


if __name__ == "__main__":
    print Solution().subsets([1, 2, 3])
