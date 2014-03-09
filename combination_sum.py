#coding: utf-8

'''
http://oj.leetcode.com/problems/combination-sum/

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is: [7] [2, 2, 3]
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates = sorted(set(candidates))
        d = [False for i in range(target + 1)]
        d[0] = True
        p = [[] for i in range(target + 1)]
        for j, x in enumerate(candidates):
            for i in range(1, target + 1):
                if i >= x and d[i - x]:
                    d[i] = True
                    p[i].append(j)

        result = []
        a = [None for i in range(target + 1)]

        def dfs(i, last, dep):
            if i == 0:
                result.append(a[:dep][::-1])
            for j in p[i]:
                if j <= last:
                    a[dep] = candidates[j]
                    dfs(i - candidates[j], j, dep + 1)

        dfs(target, len(candidates), 0)

        return result


if __name__ == "__main__":
    s = Solution()
    # print s.combinationSum([2, 3, 6, 7], 7)
    print s.combinationSum([8, 7, 4, 3], 11)

