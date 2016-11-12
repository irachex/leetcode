'''
https://leetcode.com/problems/non-overlapping-intervals/

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        it = iter(intervals)
        end, cnt = next(it).end, 0
        for x in it:
            if x.start < end:  # overlap
                cnt += 1
                end = min(end, x.end)  # erase interval with larger end
            else:
                end = x.end
        return cnt


if __name__ == '__main__':
    from utils import Interval
    f = Solution().eraseOverlapIntervals
    assert f(Interval.make_list([[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]])) == 4
    assert f(Interval.make_list([[0,2],[1,3],[2,4],[3,5],[4,6]])) == 2
    assert f(Interval.make_list([[1,100],[11,22],[1,11],[2,12]])) == 2
    assert f(Interval.make_list([ [1,2], [2,3], [3,4], [1,3] ])) == 1
    assert f(Interval.make_list([ [1,2], [1,2], [1,2] ])) == 2
    assert f(Interval.make_list([ [1,2], [2,3] ])) == 0
