'''
https://leetcode.com/problems/valid-perfect-square/

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Returns: True

Example 2:
Input: 14
Returns: False
'''

class Solution(object):

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while x * x > num:
            x = (x + num / x) / 2
        return x * x == num

    def isPerfectSquare2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = float(num)
        delta = num
        while delta > 0.01:
            new_x = (x + num / x) / 2.0
            delta = x - new_x
            x = new_x
        return abs(x - int(x)) <= delta


if __name__ == '__main__':
    f = Solution().isPerfectSquare
    assert f(1)
    assert f(16)
    assert not f(14)
    assert not f(15)
    assert f(25)
    assert f(9)
