'''
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
'''


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_sort(a, left, right):
            if left >= right:
                return
            mid = (left + right) / 2
            merge_sort(a, left, mid)
            merge_sort(a, mid + 1, right)

            t = []
            p1, p2 = left, mid + 1
            while p1 <= mid or p2 <= right:
                if p2 > right or p1 <= mid and a[p1] > a[p2]:
                    ans[a[p1][1]] += right - p2 + 1
                    t.append(a[p1])
                    p1 += 1
                elif p1 > mid or p2 <= right and a[p2] >= a[p1]:
                    t.append(a[p2])
                    p2 += 1
                else:
                    break
            for i in xrange(left, right + 1):
                a[i] = t[i - left]

        n = len(nums)
        ans = [0 for i in xrange(n)]
        a = [(x, i) for i, x in enumerate(nums)]
        merge_sort(a, 0, n - 1)
        return ans


if __name__ == '__main__':
    f = Solution().countSmaller
    assert f([]) == []
    assert f([5, 2, 6, 1]) == [2, 1, 1, 0]
