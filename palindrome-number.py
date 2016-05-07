'''
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x > 0 and x % 10 == 0:
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x /= 10
        return x == y or y / 10 == x


if __name__ == '__main__':
    f = Solution().isPalindrome
    assert f(123454321)
    assert f(12344321)
    assert not f(123443210)
    assert f(1)
    assert f(0)
    assert not f(12334321)
