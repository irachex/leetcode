'''
https://leetcode.com/problems/rectangle-area/

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
'''

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        def area(x1, y1, x2, y2):
            return (x2 - x1) * (y2 - y1) if x1 < x2 and y1 < y2 else 0

        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)
        return area(A, B, C, D) + area(E, F, G, H) - area(x1, y1, x2, y2)


if __name__ == '__main__':
    f = Solution().computeArea
    assert f(-2, -2, 2, 2, -2, -2, 2, 2) == 16
    assert f(0, 0, 0, 0, -1, -1, 1, 1) == 4
