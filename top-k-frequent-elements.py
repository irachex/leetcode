# coding: utf-8

'''
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


class MinHeap(object):

    def __init__(self, size):
        self.size = size
        self.a = []

    def add(self, x):
        if len(self.a) < self.size:
            self.a.append(x)
            self.shift_up(len(self.a) - 1)
        else:
            if x > self.a[0]:
                self.a[0] = x
                self.shift_down(0)

    def shift_up(self, i):
        a = self.a
        while i > 0:
            p = (i - 1) / 2
            if a[i] < a[p]:
                tmp = a[i]
                a[i] = a[p]
                a[p] = tmp
            i = p

    def shift_down(self, i):
        a = self.a
        while i < self.size:
            lc = i * 2 + 1
            rc = i * 2 + 2
            print i, lc, rc, len(self.a), self.size
            if lc < self.size and a[lc] < a[i] and (rc >= self.size or a[lc] <= a[rc]):
                tmp = a[i]
                a[i] = a[lc]
                a[lc] = tmp
                i = lc
            elif rc < self.size and a[rc] < a[i] and (lc >= self.size or a[rc] <= a[lc]):
                tmp = a[i]
                a[i] = a[rc]
                a[rc] = tmp
                i = rc
            else:
                break

    def __iter__(self):
        return iter(reversed(self.a))


class Solution(object):

    def topKFrequent(self, nums, k):  # counter sort
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1

        n = len(nums)
        c = [0 for i in xrange(n + 1)]
        for x, cnt in d.iteritems():
            c[cnt] += 1
        for i in xrange(1, n + 1):
            c[i] += c[i - 1]
        a = [None for i in xrange(n + 1)]
        for x, cnt in d.iteritems():
            a[c[cnt]] = x
            c[cnt] -= 1
        return [x for x in reversed(a) if x is not None][:k]

    def topKFrequent_Heap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1

        h = MinHeap(k)
        for x, cnt in d.iteritems():
            h.add((cnt, x))
        return [x for _, x in h]


if __name__ == '__main__':
    f = Solution().topKFrequent
    print f([1], 1)
    print f([5,2,5,3,5,3,1,1,3], 2)
    print f([4,1,-1,2,-1,2,3], 2)
    assert f([1,1,1,2,2,3], 2) == [1, 2]
    assert f([], 2) == []
