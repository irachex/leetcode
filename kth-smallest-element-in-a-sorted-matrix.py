# coding: utf-8

'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n^2.
'''


class Heap(object):

    def __init__(self, n):
        self.a = [0 for i in xrange(n)]
        self.num = 0

    def push(self, x):
        i = self.num
        self.a[i] = x
        self.num += 1
        self.shift_up(i)

    def pop(self):
        top = self.a[0]
        self.swap(0, self.num - 1)
        self.num -= 1
        self.shift_down(0)
        return top

    def shift_up(self, i):
        while i > 0 and self.a[i] < self.a[(i - 1) / 2]:
            self.swap(i, (i - 1) / 2)
            i = (i - 1) / 2

    def shift_down(self, i):
        while i * 2 + 1 < self.num:
            if (i * 2 + 2 < self.num and
                    self.a[i] > self.a[i * 2 + 2] and
                    self.a[i * 2 + 2] < self.a[i * 2 + 1]):
                self.swap(i, i * 2 + 2)
                i = i * 2 + 2
            elif self.a[i] > self.a[i * 2 + 1]:
                self.swap(i, i * 2 + 1)
                i = i * 2 + 1
            else:
                break

    def swap(self, x, y):
        tmp = self.a[x]
        self.a[x] = self.a[y]
        self.a[y] = tmp

    def __repr__(self):
        return repr(self.a[:self.num])


class Solution(object):
    def kthSmallest(self, matrix, k):  # binary search, O(NlogN)
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        ans = 0
        left, right = matrix[0][0], matrix[n - 1][m - 1]
        while left <= right:
            mid = (left + right) / 2
            # count less than mid
            cnt = 0
            j = m
            for i in xrange(n):
                while j > 0 and matrix[i][j - 1] > mid:
                    j -= 1
                cnt += j
            if cnt < k:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        return ans

    def kthSmallest_Heap(self, matrix, k):  # Heap, O(KlogN)
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        heap = Heap(n)
        for i, x in enumerate(matrix[0]):
            heap.push((x, 0, i))
        for i in xrange(k - 1):
            v, x, y = heap.pop()
            if x + 1 < n:
                x += 1
                heap.push((matrix[x][y], x, y))
        return heap.pop()[0]

    # There is a O(N) algorithm to this problem
    # http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf
    # https://en.wikipedia.org/wiki/Median_of_medians


if __name__ == '__main__':
    f = Solution().kthSmallest
    m = [[1,  5,  9],
         [10, 11, 13],
         [12, 13, 15]]
    assert f(m, 1) == 1
    assert f(m, 6) == 12
    assert f(m, 7) == 13
    assert f(m, 8) == 13
    assert f(m, 9) == 15

    m = [[ 1, 4, 7,11,15],
         [ 2, 5, 8,12,19],
         [ 3, 6, 9,16,22],
         [10,13,14,17,24],
         [18,21,23,26,30]]
    assert f(m, 20) == 21
