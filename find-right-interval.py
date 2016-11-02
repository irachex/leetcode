'''
https://leetcode.com/problems/find-right-interval/

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
Example 1:
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
Example 3:
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        a = list(enumerate(intervals))
        a.sort(key=lambda (i, x): x.start)
        b = list(enumerate(intervals))
        b.sort(key=lambda (i, x): x.end)

        n = len(intervals)
        k = 0
        r = [-1 for i in xrange(n)]
        for i, x in b:
            if k < n and x.end <= a[k][1].start:
                r[i] = a[k][0]
            else:
                while k < n and x.end > a[k][1].start:
                    k += 1
                if k < n:
                    r[i] = a[k][0]
                else:
                    r[i] = -1
        return r


if __name__ == '__main__':
    from utils import Interval

    f = Solution().findRightInterval
    assert f(Interval.make_list([ [1,2] ])) == [-1]
    assert f(Interval.make_list([ [3,4], [2,3], [1,2] ])) == [-1, 0, 1]
    assert f(Interval.make_list([ [1,4], [2,3], [3,4] ])) == [-1, 2, -1]
