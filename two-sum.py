#coding: utf-8

'''
http://oj.leetcode.com/problems/two-sum/

Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9Output: index1=1, index2=2
'''

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i, x in enumerate(num):
            d[x] = i
        for i, x in enumerate(num):
            j = d.get(target - x)
            if j is not None and j != i:
                return (i + 1, j + 1) if i < j else (j + 1, i + 1)


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == (1, 2)
    assert s.twoSum([3, 2, 4], 6) == (2, 3)
