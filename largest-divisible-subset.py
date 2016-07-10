'''
https://leetcode.com/problems/largest-divisible-subset/

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
nums: [1,2,3]
Result: [1,2] (of course, [1,3] will also be ok)

Example 2:
nums: [1,2,4,8]
Result: [1,2,4,8]
'''

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums.sort()
        d = [1 for i in xrange(n)]
        p = [-1 for i in xrange(n)]
        max_d = 1
        k = 0 if n > 0 else -1
        for i in xrange(1, n):
            for j in xrange(i):
                if nums[i] % nums[j] == 0 and d[i] < d[j] + 1:
                    d[i] = d[j] + 1
                    p[i] = j
            if max_d < d[i]:
                max_d = d[i]
                k = i
        r = []
        while k != -1:
            r.append(nums[k])
            k = p[k]
        return list(reversed(r))


if __name__ == '__main__':
    f = Solution().largestDivisibleSubset
    assert f([1]) == [1]
    assert f([]) == []
    assert f([1, 2, 3]) == [1, 2]
    assert f([1, 2, 4, 8]) == [1, 2, 4, 8]
