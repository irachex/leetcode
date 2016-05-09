'''
https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[%s, %s]' % (self.start, self.end)


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        s = newInterval.start
        e = newInterval.end
        i = 0
        inserted = False
        while i < len(intervals):
            itv = intervals[i]
            if (itv.start <= s <= itv.end or
                    itv.start <= e <= itv.end or
                    s <= itv.start and e >= itv.end):
                while i < len(intervals):
                    itv = intervals[i]
                    if (itv.start <= s <= itv.end or
                            itv.start <= e <= itv.end or
                            s <= itv.start and e >= itv.end):
                        s = min(s, itv.start)
                        e = max(e, itv.end)
                    else:
                        break
                    i += 1
            else:
                if not inserted and itv.start > e:
                    result.append(Interval(s, e))
                    inserted = True
                result.append(itv)
                i += 1
        if not inserted:
            result.append(Interval(s, e))
        return result


def solve(intervals, interval):
    intervals = [Interval(s, e) for s, e in intervals]
    interval = Interval(interval[0], interval[1])
    r = Solution().insert(intervals, interval)
    return [[i.start, i.end] for i in r]

if __name__ == '__main__':
    assert solve([[2,5],[6,7],[8,9]], [0,1]) == [[0,1],[2,5],[6,7],[8,9]]
    assert solve([[1, 2]], [4,5]) == [[1,2], [4,5]]
    assert solve([[4, 5]], [1,2]) == [[1,2], [4,5]]
    assert solve([], [1,5]) == [[1,5]]
    assert solve([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert solve([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]) == [[1,2],[3,10],[12,16]]
