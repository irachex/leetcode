# coding: utf-8

'''
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
'''


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda (s, e): (s, -e))
        cnt = 1
        curr_end = points[0][1]
        for i in xrange(1, len(points)):
            start, end = points[i]
            if start <= curr_end:
                curr_end = min(curr_end, end)
            else:
                cnt += 1
                curr_end = end
        return cnt


if __name__ == '__main__':
    f = Solution().findMinArrowShots
    assert f([[1,2],[2,3],[3,4],[4,5]]) == 2
    assert f([[10,16], [2,8], [1,6], [7,12]]) == 2
