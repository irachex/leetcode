#coding: utf-8

'''
http://oj.leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.\n
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: (x.start, x.end))
        result = []
        first = intervals[0]
        current = Interval(first.start, first.end)
        for a in intervals[1:]:
            if a.start > current.end:
                result.append(current)
                current = Interval(a.start, a.end)
            elif a.end > current.end:
                current.end = a.end
        result.append(current)
        return result


if __name__ == "__main__":
    print Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
