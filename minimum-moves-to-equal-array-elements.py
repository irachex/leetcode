'''
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
'''


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        min_v = min(nums)
        return sum([x - min_v for x in nums])


if __name__ == '__main__':
    f = Solution().minMoves
    assert f([1, 2, 3]) == 3
