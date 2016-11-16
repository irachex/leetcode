# coding: utf-8

'''
https://leetcode.com/problems/split-array-largest-sum/

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
Given m satisfies the following constraint: 1 ≤ m ≤ length(nums) ≤ 14,000.

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def ok(limit):
            cnt = 1
            s = 0
            for x in nums:
                if s + x <= limit:
                    s += x
                elif x <= limit:
                    s = x
                    cnt += 1
                    if cnt > m:
                        return False
                else:
                    return False
            return cnt <= m

        s = sum(nums)
        ans = s
        left, right = max(s / m, max(nums)), s
        while left <= right:
            mid = (left + right) / 2
            if ok(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


if __name__ == '__main__':
    f = Solution().splitArray
    assert f([1,2147483647], 2) == 2147483647
    # assert f([7,2,5,10,8], 2) == 18
