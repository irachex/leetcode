# coding: utf-8

'''
https://leetcode.com/problems/h-index/

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n = len(citations)
        d = [0 for i in xrange(n + 1)]
        for i, ai in enumerate(citations):
            if ai >= n:
                d[n] += 1
            else:
                d[ai] += 1

        s = 0
        for i in reversed(xrange(n + 1)):
            s += d[i]
            if s >= i:
                return i
        return 0

    def hIndex_binary_search(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        citations.sort()
        ans = 0
        n = len(citations)
        left, right = 0, n
        while left <= right:
            mid = (left + right) / 2
            if mid == 0 or citations[n - mid] >= mid:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


if __name__ == '__main__':
    f = Solution().hIndex
    assert f([3, 0, 6, 1, 5]) == 3
    assert f([0, 0, 0, 0, 5]) == 1
