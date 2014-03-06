#coding: utf-8

'''
http://oj.leetcode.com/problems/plus-one/

Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        plus = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += plus
            if digits[i] >= 10:
                digits[i] -= 10
                plus = 1
            else:
                plus = 0
                break
        if plus:
            digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    s = Solution()
    assert s.plusOne([9]) == [1, 0]
