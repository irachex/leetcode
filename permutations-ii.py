'''
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        nums.sort()
        a = []
        cnt = 1
        x = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] != x:
                a.append([x, cnt])
                x = nums[i]
                cnt = 1
            else:
                cnt += 1
        a.append([x, cnt])

        def dfs(i, s, last):
            if i == n:
                result.append(s[:])
                return
            for j in xrange(m):
                if a[j][0] == last:
                    continue
                for k in xrange(1, a[j][1] + 1):
                    a[j][1] -= k
                    dfs(i + k, s + [a[j][0]] * k, a[j][0])
                    a[j][1] += k

        n = len(nums)
        m = len(a)
        result = []
        dfs(0, [], None)
        return result


if __name__ == '__main__':
    f = Solution().permuteUnique
    print f([1, 1, 2])
