# coding: utf-8

'''
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

import random


class Solution(object):
    def findKthLargest_heap(self, nums, k):  # O(NlogK)
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest(self, nums, k):  # O(N) in average
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        random.shuffle(nums)
        return quickselect2(nums, 0, n - 1, n - k + 1)


def quickselect(a, start, end, k):
    i, j, pivot = start, end, a[start]
    while i < j:
        while i < j and a[j] >= pivot:
            j -= 1
        a[i] = a[j]
        while i < j and a[i] < pivot:
            i += 1
        a[j] = a[i]
    a[i] = pivot
    if i == k - 1:
        return a[i]
    elif i > k - 1:
        return quickselect(a, start, i - 1, k)
    else:
        return quickselect(a, i + 1, end, k)


def quickselect2(a, left, right, k):
    if left == right:
        return a[left]
    pivot = random.randint(left, right)
    a[left], a[pivot] = a[pivot], a[left]

    i = left
    for j in xrange(left + 1, right + 1):
        if a[j] < a[left]:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i], a[left] = a[left], a[i]

    if i == k - 1:
        return a[i]
    elif i > k - 1:
        return quickselect2(a, left, i - 1, k)
    else:
        return quickselect2(a, i + 1, right, k)


if __name__ == '__main__':
    f = Solution().findKthLargest
    assert f([99, 99], 1) == 99
    assert f([2, 1], 2) == 1
    assert f([-1, -1], 2) == -1
    assert f([1], 1) == 1
    assert f([3, 2, 1, 5, 6, 4], 2) == 5
