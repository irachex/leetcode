'''
https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        d = [[0 for j in xrange(m)] for i in xrange(n)]
        dcol = [0 for j in xrange(m)]
        ans = 0
        for i in xrange(n):
            drow = 0
            for j in xrange(m):
                if int(matrix[i][j]):
                    drow += 1
                    dcol[j] += 1
                    d[i][j] = min(d[i - 1][j - 1] + 1, drow, dcol[j]) if i > 0 and j > 0 else 1
                    ans = max(ans, d[i][j] * d[i][j])
                else:
                    d[i][j] = drow = dcol[j] = 0
        return ans


if __name__ == '__main__':
    f = Solution().maximalSquare
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
    ]
    assert f(matrix) == 4
    assert f(["0"]) == 0
