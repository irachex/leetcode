'''
https://leetcode.com/problems/3sum-closest/

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in xrange(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(ans - target):
                    ans = s
                    if ans == target:
                        return ans
                if s > target:
                    k -= 1
                else:
                    j += 1
        return ans


if __name__ == '__main__':
    f = Solution().threeSumClosest
    assert f([-1, 2, 1, -4], 1) == 2
    assert f([0, 1, 2], 3) == 3
