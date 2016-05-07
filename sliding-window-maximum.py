# coding: utf-8

'''
https://leetcode.com/problems/sliding-window-maximum/

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
'''

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        r = []
        q = [(0, 0) for i in xrange(len(nums))]
        head = 0
        tail = -1
        for i, x in enumerate(nums):
            while head <= tail and q[head][0] <= i - k:
                head += 1
            if i >= k - 1:
                if k > 1:
                    r.append(max(q[head][1], x))
                else:
                    r.append(x)
            while head <= tail and q[tail][1] < x:
                tail -= 1
            tail += 1
            q[tail] = (i, x)
        return r


if __name__ == '__main__':
    f = Solution().maxSlidingWindow
    assert f([1,3,-1,-3,5,3,6,7], 3) == [3, 3, 5, 5, 6, 7]

    assert f([1, -1], 1) == [1, -1]
