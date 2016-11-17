'''
https://leetcode.com/problems/132-pattern/

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]
Output: False
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: [3, 1, 4, 2]
Output: True
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: [-1, 3, 2, 0]
Output: True
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a3 = -(1 << 31)
        stack = []
        for x in reversed(nums):
            if x < a3:  # found a1
                return True
            else:
                while stack and x > stack[-1]:
                    a3 = max(a3, stack.pop())
                stack.append(x)  # x is a2
        return False


if __name__ == '__main__':
    f = Solution().find132pattern
    assert not f([1, 2, 3, 4])
    assert f([3, 1, 4, 2])
    assert f([-1, 3, 2, 0])
