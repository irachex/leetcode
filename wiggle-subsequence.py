'''
https://leetcode.com/problems/wiggle-subsequence/

A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
'''

class Solution(object):

    def wiggleMaxLength(self, nums):  # O(N) Time, O(1) Space
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        up = down = 1
        for i in xrange(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down) if n else 0

    def wiggleMaxLength_N(self, nums):  # O(N)
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        up = [1 for x in range(n)]
        down = [1 for x in range(n)]
        for i in xrange(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return max(up[n - 1], down[n - 1]) if n else 0

    def wiggleMaxLength_N2(self, nums):  # O(N^2)
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        d = [[1, 1] for i in xrange(n)]
        for i in xrange(1, n):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    d[i][0] = max(d[i][0], d[j][1] + 1)
                elif nums[i] < nums[j]:
                    d[i][1] = max(d[i][1], d[j][0] + 1)
        return max(max(row) for row in d) if d else 0


if __name__ == '__main__':
    f = Solution().wiggleMaxLength
    assert f([]) == 0
    assert f([1,7,4,9,2,5]) == 6
    assert f([1,17,5,10,13,15,10,5,16,8]) == 7
    assert f([1,2,3,4,5,6,7,8,9]) == 2
