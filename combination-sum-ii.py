# coding: utf-8

'''
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        a = []
        x, cnt = candidates[0], 1
        for i in xrange(1, len(candidates)):
            if x == candidates[i]:
                cnt += 1
            else:
                a.append((x, cnt))
                x, cnt = candidates[i], 1
        a.append((x, cnt))
        n = len(a)

        def dfs(dep, last, s):
            if s == target:
                p = []
                for i in xrange(dep):
                    x, cnt = c[i]
                    p.extend([x for k in xrange(cnt)])
                result.append(p)
                return

            for j in xrange(last + 1, n):
                x, cnt = a[j]
                if s + x > target:
                    break
                for k in xrange(1, cnt + 1):
                    c[dep] = (x, k)
                    t = s + k * x
                    if t <= target:
                        dfs(dep + 1, j, t)
                    else:
                        break

        c = [None for i in xrange(n)]
        result = []
        dfs(0, -1, 0)
        return result


if __name__ == '__main__':
    f = Solution().combinationSum2
    print f([2,5,2,1,2], 5)
    print f([10,1,2,7,6,1,5], 8)
