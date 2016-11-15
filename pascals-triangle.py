#coding: utf-8

'''
http://oj.leetcode.com/problems/pascals-triangle/

Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        a = [[1]]
        for i in range(1, numRows):
            a.append([0 for j in range(i + 1)])
            for j in range(i + 1):
                if j == 0 or j == i:
                    a[i][j] = 1
                else:
                    a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
        return a


if __name__ == "__main__":
    print Solution().generate(5)
