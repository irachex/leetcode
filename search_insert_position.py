# coding: utf-8

"""
http://oj.leetcode.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for i, x in reversed(list(enumerate(A))):
            if x < target:
                return i + 1
        return 0


if __name__ == "__main__":
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.searchInsert([1, 3, 5, 6], 0) == 0
