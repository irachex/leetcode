'''
https://leetcode.com/problems/find-median-from-data-stream/

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2
'''

import heapq


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.smaller = []
        self.larger = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        x = heapq.heappushpop(self.larger, num)
        heapq.heappush(self.smaller, -x)
        if len(self.larger) < len(self.smaller):
            heapq.heappush(self.larger, -heapq.heappop(self.smaller))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        return (self.larger[0] if len(self.larger) > len(self.smaller)
                else (self.larger[0] - self.smaller[0]) / 2.0)


if __name__ == '__main__':
    m = MedianFinder()
    m.addNum(1)
    assert m.findMedian() == 1
    m.addNum(2)
    assert m.findMedian() == (1 + 2) / 2.0
    m.addNum(3)
    assert m.findMedian() == 2
