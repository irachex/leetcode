'''
https://leetcode.com/problems/4sum/

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []
        for i in xrange(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                x = j + 1
                y = n - 1
                while x < y:
                    s = nums[i] + nums[j] + nums[x] + nums[y]
                    if s > target:
                        y -= 1
                    elif s < target:
                        x += 1
                    else:
                        result.append([nums[i], nums[j], nums[x], nums[y]])
                        x += 1
                        y -= 1
                        while x < y and nums[x] == nums[x - 1]:
                            x += 1
                        while x < y and nums[y] == nums[y + 1]:
                            y -= 1
        return result


if __name__ == '__main__':
    f = Solution().fourSum
    print f([1, -2, -5, -4, -3, 3, 3, 5], -11)
    assert len(f([1, 0, -1, 0, -2, 2], 0)) == 3
