'''
https://leetcode.com/problems/h-index-ii/

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

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
