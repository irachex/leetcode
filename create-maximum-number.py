'''
https://leetcode.com/problems/create-maximum-number/

Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
'''

import collections


class Solution(object):
    def maxNumber(self, nums1, nums2, k):  # O(k(n + m))
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def single_max_number(a, k):
            drop = len(a) - k
            stack = []
            for x in a:
                while stack and drop > 0 and x > stack[-1]:
                    drop -= 1
                    stack.pop()
                stack.append(x)
            return stack[:k]

        def merge(a, b):
            a, b = collections.deque(a), collections.deque(b)
            c = []
            while a and b:
                if a > b:
                    c.append(a.popleft())
                else:
                    c.append(b.popleft())
            if a:
                c.extend(a)
            elif b:
                c.extend(b)
            return c

        ans = []
        for k1 in xrange(k + 1):
            n1 = single_max_number(nums1, k1)
            n2 = single_max_number(nums2, k - k1)
            x = merge(n1, n2)
            if len(ans) < len(x) or len(ans) == len(x) and ans < x:
                ans = x
        return ans

    def maxNumber_DP(self, nums1, nums2, k):  # O(nmk) TLE
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums1)
        m = len(nums2)
        d = [[['' for x in xrange(k + 1)] for j in xrange(m + 1)] for i in xrange(n + 1)]
        for i in xrange(n + 1):
            for j in xrange(m + 1):
                for x in xrange(1, k + 1):
                    if i > 0:
                        d[i][j][x] = max(d[i][j][x], d[i - 1][j][x], d[i - 1][j][x - 1] + str(nums1[i - 1]))
                    if j > 0:
                        d[i][j][x] = max(d[i][j][x], d[i][j - 1][x], d[i][j - 1][x - 1] + str(nums2[j - 1]))
        return map(int, d[n][m][k])


if __name__ == '__main__':
    f = Solution().maxNumber
    assert f([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5) == [9, 8, 6, 5, 3]
    assert f([6, 7], [6, 0, 4], 5) == [6, 7, 6, 0, 4]
    assert f([3, 9], [8, 9], 3) == [9, 8, 9]
