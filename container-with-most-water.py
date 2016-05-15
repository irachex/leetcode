'''
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                area = (right - left) * height[left]
                left += 1
            else:
                area = (right - left) * height[right]
                right -= 1
            ans = max(ans, area)
        return ans
