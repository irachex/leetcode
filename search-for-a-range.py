#coding: utf-8

'''
http://oj.leetcode.com/problems/search-for-a-range/

Given a sorted array of integers, find the starting and ending position of a given target value.\nYour algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if not A:
            return [-1, -1]
        n = len(A)
        left = 0
        right = n - 1
        a = None
        while left <= right:
            mid = (left + right) / 2
            if target > A[mid]:
                left = mid + 1
                a = mid
            elif target <= A[mid]:
                right = mid - 1

        a = a or right
        if a + 1 >= n or A[a + 1] != target:
            return [-1, -1]
        a += 1

        left = 0
        right = n - 1
        b = None
        while left <= right:
            mid = (left + right) / 2
            if target >= A[mid]:
                left = mid + 1
            elif target < A[mid]:
                right = mid - 1
                b = mid

        b = b or left
        if b - 1 < 0 or A[b - 1] != target:
            return [-1, -1]
        b -= 1

        return [a, b]


if __name__ == "__main__":
    s = Solution()
    assert s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 7) == [1, 2]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 5) == [0, 0]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 4) == [-1, -1]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 16) == [-1, -1]
