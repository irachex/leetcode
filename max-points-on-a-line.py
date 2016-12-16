'''
https://leetcode.com/problems/max-points-on-a-line/

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    @classmethod
    def make_list(cls, data):
        return [cls(x, y) for x, y in data]


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        if n <= 1:
            return n

        def gcd(x, y):
            return gcd(y, x % y) if y else x

        ans = 0
        for i in xrange(n):
            d = {}
            cnt = overlap = 0
            for j in xrange(n):
                y = points[i].y - points[j].y
                x = points[i].x - points[j].x
                if x == 0 and y == 0:
                    overlap += 1
                    continue
                g = gcd(x, y)
                key = (y / g if g else y, x / g if g else x)
                d[key] = d.get(key, 0) + 1
                cnt = max(cnt, d[key])
            ans = max(ans, cnt + overlap)
        return ans


if __name__ == '__main__':
    f = Solution().maxPoints
    assert f(Point.make_list([[0,0],[1,1],[0,0]])) == 3
    assert f(Point.make_list([(1, 0), (2, 0), (3, 0)])) == 3
    assert f(Point.make_list([(0, 1), (0, 2), (0, 3)])) == 3
    assert f(Point.make_list([[1,1],[1,1],[2,2],[2,2]])) == 4
    assert f(Point.make_list([(0, 0), (1, 1), (2, 2), (3, 4)])) == 3
    assert f(Point.make_list([(3, 5), (1, 1), (2, 2), (3, 4)])) == 2
