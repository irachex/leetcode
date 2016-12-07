'''
https://leetcode.com/problems/perfect-rectangle/

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
'''


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        maxx = maxy = -(1 << 30)
        minx = miny = 1 << 30
        s = 0
        points = {}
        for (x1, y1, x2, y2) in rectangles:
            minx = min(minx, x1)
            miny = min(miny, y1)
            maxx = max(maxx, x2)
            maxy = max(maxy, y2)
            s += (x2 - x1) * (y2 - y1)
            points[(x1, y1)] = points.get((x1, y1), 0) + 1
            points[(x1, y2)] = points.get((x1, y2), 0) + 1
            points[(x2, y1)] = points.get((x2, y1), 0) + 1
            points[(x2, y2)] = points.get((x2, y2), 0) + 1
        for x, y in [(minx, miny), (minx, maxy), (maxx, miny), (maxx, maxy)]:
            if points.get((x, y)) != 1:
                return False
            del points[(x, y)]
        if any(v & 1 for v in points.itervalues()):
            return False
        return s == (maxx - minx) * (maxy - miny)


if __name__ == '__main__':
    f = Solution().isRectangleCover
    assert f([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]])
