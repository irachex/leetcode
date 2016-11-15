#coding: utf-8

'''
http://oj.leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up:
Could you do this in-place?
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        if n == 0:
            return matrix
        for i in range(n / 2):
            for j in range(n - i * 2 - 1):
                tmp = matrix[i][i + j]
                matrix[i][i + j] = matrix[n - 1 - i - j][i]
                matrix[n - 1 - i - j][i] = matrix[n - 1 - i][n - 1 - i - j]
                matrix[n - 1 - i][n - 1 - i - j] = matrix[i + j][n - 1 - i]
                matrix[i + j][n - 1 - i] = tmp
        return matrix

    def rotate2(self, matrix):
        n = len(matrix)
        A = [[0 for i in range(n)] for j in range(n)]
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                A[j][n - i] = matrix[i][j]
        return A


if __name__ == '__main__':
    s = Solution()
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    R = [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]

    A = s.rotate(A)
    print A
    assert A == R
