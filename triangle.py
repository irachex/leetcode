#coding: utf-8

'''
http://oj.leetcode.com/problems/triangle/

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        INF = 999999999
        n = len(triangle)
        a = [0 for i in range(n)]
        for row in triangle:
            b = [INF for i in range(n)]
            for j, x in enumerate(row):
                b[j] = min(b[j], a[j] + x)
                if j > 0:
                    b[j] = min(b[j], a[j - 1] + x)
            a = b
        return min(b)
