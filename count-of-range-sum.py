# coding: utf-8

'''
https://leetcode.com/problems/count-of-range-sum/

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
'''


class SegmentTreeNode(object):

    def __init__(self, li, ri, value=None):
        self.li = li
        self.ri = ri
        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def make_tree(cls, a, li, ri):
        node = cls(a[li], a[ri], 0)
        if li == ri:
            return node
        mid = (li + ri) / 2
        if li <= mid:
            node.left = cls.make_tree(a, li, mid)
        if mid + 1 <= ri:
            node.right = cls.make_tree(a, mid + 1, ri)
        return node

    def add(self, li, ri, value):
        if self.li == self.ri:
            self.value += value
            return
        if self.left and li <= self.left.ri:
            self.left.add(li, ri, value)
        if self.right and ri >= self.right.li:
            self.right.add(li, ri, value)
        self.value = ((self.left.value if self.left else 0) +
                      (self.right.value if self.right else 0))

    def query(self, li, ri):
        if self.li >= li and self.ri <= ri:
            return self.value
        r = 0
        if self.left and li <= self.left.ri:
            r += self.left.query(li, ri)
        if self.right and ri >= self.right.li:
            r += self.right.query(li, ri)
        return r


class Solution(object):

    def countRangeSum(self, nums, lower, upper):  # merge sort
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0

        s = [0]
        for i in xrange(1, len(nums) + 1):
            s.append(s[i - 1] + nums[i - 1])

        def merge_sort(a, left, right):
            if left >= right:
                return
            mid = (left + right) / 2
            merge_sort(a, left, mid)
            merge_sort(a, mid + 1, right)

            # count
            j = k = mid + 1
            for i in xrange(left, mid + 1):
                while j <= right and a[j] - a[i] < lower:
                    j += 1
                while k <= right and a[k] - a[i] <= upper:
                    k += 1
                ans[0] += k - j

            # merge
            t = []
            p1, p2 = left, mid + 1
            while p1 <= mid or p2 <= right:
                if p2 > right or p1 <= mid and a[p1] <= a[p2]:
                    t.append(a[p1])
                    p1 += 1
                elif p1 > mid or p2 <= right and a[p2] <= a[p1]:
                    t.append(a[p2])
                    p2 += 1
                else:
                    break
            for i in xrange(left, right + 1):
                a[i] = t[i - left]

        ans = [0]
        merge_sort(s, 0, len(s) - 1)
        return ans[0]

    def countRangeSum_SegmentTree(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0
        s = [0]
        for i in xrange(1, len(nums) + 1):
            s.append(s[i - 1] + nums[i - 1])

        sorted_s = list(sorted(set(s)))
        root = SegmentTreeNode.make_tree(sorted_s, 0, len(sorted_s) - 1)

        ans = 0
        for si in reversed(s):
            # lower <= sj - si <= upper, j > i
            ans += root.query(lower + si, upper + si)
            root.add(si, si, 1)
        return ans


if __name__ == '__main__':
    f = Solution().countRangeSum
    assert f([-2, 5, -1], -2, 2) == 3
    assert f([2147483647, -2147483648, -1, 0], -1, 0) == 4
