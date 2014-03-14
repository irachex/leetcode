#coding: utf-8

'''
http://oj.leetcode.com/problems/spiral-matrix-ii/

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
For example,
Given n = 3,
You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = [[0 for j in range(n)] for i in range(n)]
        x = y = d = 0
        for i in range(n * n):
            m[x][y] = i + 1
            tx = x + directions[d][0]
            ty = y + directions[d][1]
            if tx < 0 or ty < 0 or tx >= n or ty >= n or m[tx][ty]:
                d = (d + 1) % 4
            x += directions[d][0]
            y += directions[d][1]

        return m


if __name__ == "__main__":
    print Solution().generateMatrix(3)
