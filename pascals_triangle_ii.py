#coding: utf-8

'''
http://oj.leetcode.com/problems/pascals-triangle-ii/

Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].
Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        a = [1]
        for i in range(1, rowIndex + 1):
            b = [0 for j in range(i + 1)]
            for j in range(i + 1):
                if j == 0 or j == i:
                    b[j] = 1
                else:
                    b[j] = a[j - 1] + a[j]
            a = b
        return a
