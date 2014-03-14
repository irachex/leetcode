#coding: utf-8

'''
http://oj.leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
For example,
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        b = [[False for j in range(n)] for i in range(m)]
        x = y = d = 0
        for i in range(n * m):
            result.append(matrix[x][y])
            b[x][y] = True
            tx = x + directions[d][0]
            ty = y + directions[d][1]
            if tx < 0 or ty < 0 or tx >= m or ty >= n or b[tx][ty]:
                d = (d + 1) % 4
            x += directions[d][0]
            y += directions[d][1]

        return result


if __name__ == "__main__":
    print Solution().spiralOrder([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9]])
