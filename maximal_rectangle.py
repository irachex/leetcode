#coding: utf-8

'''
http://oj.leetcode.com/problems/maximal-rectangle/

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
'''

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        ans = 0
        height = [0 for i in range(m + 2)]
        stack = []
        for i in range(1, n + 1):
            width = [0 for j in range(m + 2)]
            for j in range(1, m + 2):
                if j <= m and matrix[i - 1][j - 1] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

                if len(stack) == 0 or height[j] >= height[stack[-1]]:
                    stack.append(j)
                    width[j] = 1
                else:
                    w = 0
                    while stack and height[j] < height[stack[-1]]:
                        width[stack[-1]] += w
                        ans = max(ans, height[stack[-1]] * width[stack[-1]])
                        w = width[stack[-1]]
                        stack.pop()
                    stack.append(j)
                    width[j] = w + 1

        return ans


if __name__ == "__main__":
    m = [
        '10001',
        '11111',
        '11111',
    ]
    print Solution().maximalRectangle(m)
