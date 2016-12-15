'''
https://leetcode.com/problems/max-sum-of-sub-matrix-no-larger-than-k/

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
'''

import bisect


class Solution(object):

    def maxSumSubmatrix(self, matrix, k):  # O(N^2*M^2)
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0]) if matrix else 0
        by_row = True
        if n > m:
            by_row = False
            tmp = n
            n = m
            m = tmp

        ans = -(1 << 31)
        for r1 in xrange(n):
            s = [0 for j in xrange(m + 1)]
            for r2 in xrange(r1, n):
                q = [0, 1 << 31]
                rs = 0
                for j in xrange(1, m + 1):
                    rs += (matrix[r2][j - 1] if by_row else matrix[j - 1][r2])
                    s[j] += rs
                    i = bisect.bisect_left(q, s[j] - k)
                    ans = max(ans, s[j] - q[i])
                    bisect.insort(q, s[j])
        return ans

    def maxSumSubmatrix_treap(self, matrix, k):  # O(N^3*logN)  O(min(N, M)^2*max(N, M)*logN)
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0]) if matrix else 0
        ans = -(1 << 31)
        for r1 in xrange(n):
            s = [0 for j in xrange(m + 1)]
            for r2 in xrange(r1, n):
                treap = Treap()
                treap.insert(0)
                rs = 0
                for j in xrange(1, m + 1):
                    rs += matrix[r2][j - 1]
                    s[j] += rs
                    si = treap.upper_bound(s[j] - k)
                    ans = max(ans, s[j] - si)
                    treap.insert(s[j])
        return ans

    def maxSumSubmatrix_brute_force(self, matrix, k):  # O(N^2*M^2)
        n = len(matrix)
        m = len(matrix[0]) if matrix else 0
        s = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]
        for i in xrange(1, n + 1):
            rs = 0
            for j in xrange(1, m + 1):
                rs += matrix[i - 1][j - 1]
                s[i][j] = s[i - 1][j] + rs
        ans = -(1 << 31)
        x1 = y1 = x2 = y2 = 0
        for i1 in xrange(n):
            for j1 in xrange(m):
                for i2 in xrange(i1, n):
                    for j2 in xrange(j1, m):
                        x = s[i2 + 1][j2 + 1] - s[i1][j2 + 1] - s[i2 + 1][j1] + s[i1][j1]
                        if x <= k and ans < x:
                            ans = x
                            x1, y1, x2, y2 = i1, j1, i2, j2
        print x1, y1, x2, y2
        return ans


import random


class TreapNode(object):

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.rand = random.randint(0, 1 << 31)

    def right_rotate(self):
        a = self
        b = a.left
        a.left = b.right
        b.right = a
        return b

    def left_rotate(self):
        a = self
        b = a.right
        a.right = b.left
        b.left = a
        return b

    def __repr__(self):
        return str(self.value)


class Treap(object):

    def __init__(self):
        self.root = None

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, p, x):
        if p is None:
            return TreapNode(x)
        if x < p.value:
            p.left = self._insert(p.left, x)
            if p.left.rand < p.rand:
                p = p.right_rotate()
        elif x > p.value:
            p.right = self._insert(p.right, x)
            if p.right.rand < p.rand:
                p = p.left_rotate()
        return p

    def upper_bound(self, x):
        return self._upper_bound(self.root, x)

    def _upper_bound(self, p, x):
        if p is None:
            return 1 << 31
        if x == p.value:
            return p.value
        elif x < p.value:
            return min(p.value, self._upper_bound(p.left, x))
        else:
            return self._upper_bound(p.right, x)

    def __repr__(self):
        stack = []

        def dfs(p):
            if p is None:
                return
            dfs(p.left)
            stack.append(p)
            dfs(p.right)

        dfs(self.root)
        return '[' + ','.join(map(str, stack)) + ']'


if __name__ == '__main__':
    f = Solution().maxSumSubmatrix
    assert f([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 8) == 8
    assert f([[1, 0, 1], [0, -2, 3]], 2) == 2
    assert f([[2, 2, -1]], 0) == -1
