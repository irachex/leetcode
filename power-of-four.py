'''
https://leetcode.com/problems/power-of-four/

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num > 1:
            if num % 4 != 0:
                return False
            num /= 4
        return num == 1

    def isPowerOfFour_bit(self, num):
        return num > 0 and (num & (num - 1)) == 0 and (num & 0x55555555) != 0
