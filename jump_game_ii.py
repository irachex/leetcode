'''
https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
'''


class Solution(object):
    def jump(self, nums):  # greedy
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        d = [0 for i in xrange(n)]
        d[0] = nums[0]
        for i in xrange(1, n):
            d[i] = max(i + nums[i], d[i - 1])
        cnt = 1
        reach = d[0]
        while reach < n - 1:
            cnt += 1
            reach = d[reach]
        return cnt

    def jump_DP(self, nums):  # O(n) DP
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] >= n - 1:
            return 1
        d = [n for i in xrange(n)]
        d[0] = 0
        q = [0 for i in xrange(n)]
        head = tail = 0
        for i in xrange(1, n):
            while head < tail and q[head] + nums[q[head]] < i:
                head += 1
            d[i] = d[q[head]] + 1
            while head <= tail and d[i] < d[q[tail]]:
                tail -= 1
            tail += 1
            q[tail] = i

            if i + nums[i] >= n - 1:
                return d[i] + 1
        return d[n - 1]


if __name__ == '__main__':
    jump = Solution().jump
    assert jump([1, 2, 3]) == 2
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([1, 2]) == 1
    assert jump([3, 2, 1]) == 1
    assert jump([0]) == 0
