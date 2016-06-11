'''
https://leetcode.com/problems/russian-doll-envelopes/

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        INF = [1 << 31, 1 << 31]
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        a = [INF for i in xrange(n + 1)]
        for i, e in enumerate(envelopes):
            left, right = 0, i + 1
            pos = left
            while left <= right:
                mid = (left + right) / 2
                if not (e[0] > a[mid][0] and e[1] > a[mid][1]):
                    right = mid - 1
                    pos = mid
                else:
                    left = mid + 1
            a[pos] = e
        ans = 0
        while ans < n and a[ans] < INF:
            ans += 1
        return ans


if __name__ == '__main__':
    f = Solution().maxEnvelopes
    assert f([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]) == 3
    assert f([[5,4],[6,4],[6,7],[2,3]]) == 3
