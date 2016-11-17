# coding: utf-8

'''
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''


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
        import random
        random.shuffle(nums)
        return quickselect(nums, 0, n - 1, n - k + 1)


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


if __name__ == '__main__':
    f = Solution().findKthLargest
    assert f([99, 99], 1) == 99
    assert f([2, 1], 2) == 1
    assert f([-1, -1], 2) == -1
    assert f([1], 1) == 1
    assert f([3,2,1,5,6,4], 2) == 5
