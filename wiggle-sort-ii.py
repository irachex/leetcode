'''
https://leetcode.com/problems/wiggle-sort-ii/

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
'''


import random


def quickselect(a, left, right, k):
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
        return quickselect(a, left, i - 1, k)
    else:
        return quickselect(a, i + 1, right, k)


class Solution(object):
    def wiggleSort(self, nums):  # O(N) Time and O(1) Memory
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        median = quickselect(nums, 0, n - 1, n / 2 + 1)  # find median

        def new_index(i):  # virtual indexing
            return (i * 2 + 1) % (n | 1)  # (0, 1, 2, 3, 4, 5) -> (1, 3, 5, 0, 2, 4)

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        # three-way-partition
        start = j = 0
        end = n - 1
        while j <= end:
            if nums[new_index(j)] > median:
                swap(new_index(start), new_index(j))
                start += 1
                j += 1
            elif nums[new_index(j)] < median:
                swap(new_index(j), new_index(end))
                end -= 1
            else:
                j += 1

    def wiggleSort_NlogN(self, nums):  # O(NlgN)
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


if __name__ == '__main__':
    f = Solution().wiggleSort
    A = [1,3,2,2,2,1,1,3,1,1,2]
    f(A)
    print A
    A = [1, 1, 2, 1, 2, 2, 1]
    f(A)
    print A
    A = [1, 5, 1, 1, 6, 4]
    f(A)
    print A
    A = [1, 3, 2, 2, 3, 1]
    f(A)
    print A
    A = [4, 5, 5, 6]
    f(A)
    print A
