#coding: utf-8

'''
http://oj.leetcode.com/problems/largest-rectangle-in-histogram/

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.\n\nAbove is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].\n\nThe largest rectangle is shown in the shaded area, which has area = 10 unit.\n\nFor example,
Given height = [2,1,5,6,2,3],
return 10.
'''

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        m = len(height)

        ans = 0
        width = [0 for j in range(m + 1)]
        stack = []
        for j in range(m + 1):
            h = height[j] if j < m else 0
            if len(stack) == 0 or h >= height[stack[-1]]:
                stack.append(j)
                width[j] = 1
            else:
                w = 0
                while stack and h < height[stack[-1]]:
                    width[stack[-1]] += w
                    ans = max(ans, height[stack[-1]] * width[stack[-1]])
                    w = width[stack[-1]]
                    stack.pop()
                stack.append(j)
                width[j] = w + 1
        return ans


if __name__ == "__main__":
    assert Solution().largestRectangleArea([2,1,5,6,2,3]) == 10
