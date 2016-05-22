'''
https://leetcode.com/problems/additive-number/

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
'''

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)

        def check(i, j):
            a = num[:i + 1]
            b = num[i + 1:j + 1]
            k = j + 1
            if k >= n:
                return False
            c = str(int(a) + int(b))
            while k < n and num.find(c, k) == k:
                k += len(c)
                a = b
                b = c
                c = str(int(a) + int(b))
            return k == n

        for i in xrange(n):
            if num[0] != '0' or i == 0:
                for j in xrange(i + 1, n):
                    if (num[i + 1] != '0' or j == i + 1) and check(i, j):
                        return True
        return False


if __name__ == '__main__':
    f = Solution().isAdditiveNumber
    assert not f('1023')
    assert f('112358')
    assert f('199100199')
    assert f('123')
    assert f('101')
    assert not f('1')
    assert not f('12')
    assert not f('')
    assert not f('111')
    assert not f('0011')
