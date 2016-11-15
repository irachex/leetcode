#coding: utf-8

'''
http://oj.leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,
Consider the following matrix:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        left = 0
        right = n - 1
        row = None
        while left <= right:
            mid = (left + right) / 2
            if target > matrix[mid][0]:
                row = mid
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                return True
        row = row or right
        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) / 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return matrix[row][left] == target


if __name__ == '__main__':
    A = [[1, 3, 5, 7],
         [10, 11, 16, 20],
         [23, 30, 34, 50]]
    s = Solution()
    assert s.searchMatrix(A, 11)
    assert not s.searchMatrix(A, -10)
    assert s.searchMatrix(A, 3)
    assert not s.searchMatrix(A, 14)
    assert s.searchMatrix(A, 50)
    assert not s.searchMatrix(A, 60)
