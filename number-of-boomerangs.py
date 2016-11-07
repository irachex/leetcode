'''
https://leetcode.com/problems/number-of-boomerangs/

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i, a in enumerate(points):
            h = {}
            for j, b in enumerate(points):
                if i == j:
                    continue
                d = (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])
                if d not in h:
                    h[d] = [j]
                else:
                    h[d].append(j)
            for k, v in h.iteritems():
                ans += len(v) * (len(v) - 1)
        return ans


if __name__ == '__main__':
    f = Solution().numberOfBoomerangs
    assert f([[0,0],[1,0],[2,0]]) == 2
