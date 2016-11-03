'''
https://leetcode.com/problems/data-stream-as-disjoint-intervals/

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from utils import Interval


class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.starts = {}
        self.ends = {}
        self.start_points = set()

    def _father(self, f, x):
        if f[x] == x:
            return x
        y = f[x] = self._father(f, f[x])
        return y

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.starts:
            return
        self.starts[val] = self.ends[val] = val
        self.start_points.add(val)
        if val + 1 in self.starts:
            self.starts[val + 1] = self._father(self.starts, val)
            self.ends[val] = self._father(self.ends, self.ends[val + 1])
        if val - 1 in self.starts:
            self.starts[val] = self._father(self.starts, val - 1)
            self.ends[val - 1] = self._father(self.ends, self.ends[val])

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        r = []
        for x in sorted(self.start_points):
            if x == self._father(self.starts, x):
                r.append(Interval(x, self._father(self.ends, x)))
            else:
                self.start_points.remove(x)
        return r


if __name__ == '__main__':
    s = SummaryRanges()
    for x in [1, 3, 7, 2, 6]:
        s.addNum(x)
        print s.getIntervals()
