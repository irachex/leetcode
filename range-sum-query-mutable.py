# coding: utf-8

'''
https://leetcode.com/problems/range-sum-query-mutable/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''


class SegmentTreeNode(object):

    def __init__(self, li, ri, value=None):
        self.li = li
        self.ri = ri
        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def make_tree(cls, li, ri):
        node = cls(li, ri, 0)
        if li == ri:
            return node
        mid = (li + ri) / 2
        if li <= mid:
            node.left = cls.make_tree(li, mid)
        if mid + 1 <= ri:
            node.right = cls.make_tree(mid + 1, ri)
        return node

    def update(self, i, value):
        if self.li == i and self.ri == i:
            self.value = value
            return
        if self.left and i <= self.left.ri:
            self.left.update(i, value)
        if self.right and i >= self.right.li:
            self.right.update(i, value)
        self.value = ((self.left.value if self.left else 0) +
                      (self.right.value if self.right else 0))

    def query(self, li, ri):
        if self.li >= li and self.ri <= ri:
            return self.value
        v = 0
        if self.left and li <= self.left.ri:
            v += self.left.query(li, ri)
        if self.right and ri >= self.right.li:
            v += self.right.query(li, ri)
        return v


class NumArray_SegmentTree(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.root = SegmentTreeNode.make_tree(0, len(nums))
        for i, x in enumerate(nums):
            self.root.update(i, x)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.root.update(i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.root.query(i, j)


class BinaryIndexedTree(object):

    def __init__(self, n):
        self.n = n
        self.a = [0 for i in range(n + 1)]

    def add(self, i, value):
        while i <= self.n:
            self.a[i] += value
            i += self.lowbit(i)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.a[i]
            i -= self.lowbit(i)
        return s

    def lowbit(self, x):
        return x & -x


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.BIT = BinaryIndexedTree(len(nums))
        self.nums = nums
        for i, x in enumerate(nums):
            self.BIT.add(i + 1, x)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.BIT.add(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.BIT.sum(j + 1) - self.BIT.sum(i)


if __name__ == '__main__':
    numArray = NumArray([1, 3, 5])
    assert numArray.sumRange(0, 2) == 9
    assert numArray.sumRange(0, 1) == 4
    numArray.update(1, 10)
    assert numArray.sumRange(0, 1) == 11
    assert numArray.sumRange(1, 2) == 15
    assert numArray.sumRange(0, 2) == 16
