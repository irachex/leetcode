'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i, j = 0, n - 1
        while i < j:
            v = numbers[i] + numbers[j]
            if v == target:
                return [i + 1, j + 1]
            if v < target:
                i += 1
            elif v > target:
                j -= 1


if __name__ == '__main__':
    f = Solution().twoSum
    assert f([2, 7, 11, 15], 9) == [1, 2]
    assert f([2, 7, 11, 15], 18) == [2, 3]
