'''
https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        def dfs(i, s):
            if i == n:
                result.append(s[:])
                return
            x, cnt = a[i]
            t = []
            for j in xrange(cnt + 1):
                if j > 0:
                    t.append(x)
                dfs(i + 1, s + t)

        nums.sort()
        a = []
        cnt = 1
        x = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] != x:
                a.append((x, cnt))
                x = nums[i]
                cnt = 1
            else:
                cnt += 1
        a.append((x, cnt))

        n = len(a)
        result = []
        dfs(0, [])
        return result


if __name__ == '__main__':
    f = Solution().subsetsWithDup
    print f([1, 2, 2])
