#coding: utf-8

'''
http://oj.leetcode.com/problems/set-matrix-zeroes/

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
click to show follow up.
Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix:
            return
        n = len(matrix)
        m = len(matrix[0])
        has_zero_first_row = any(matrix[0][j] == 0 for j in range(m))
        has_zero_first_col = any(matrix[i][0] == 0 for i in range(n))

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if has_zero_first_row:
            for j in range(m):
                matrix[0][j] = 0
        if has_zero_first_col:
            for i in range(n):
                matrix[i][0] = 0


if __name__ == "__main__":
    matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    Solution().setZeroes(matrix)
    print matrix
