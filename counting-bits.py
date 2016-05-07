# coding: utf-8

'''
https://leetcode.com/problems/counting-bits/

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        a = [0 for i in xrange(num + 1)]
        for i in xrange(1, num + 1):
            a[i] = a[i >> 1] + (i & 1)
        return a


if __name__ == '__main__':
    f = Solution().countBits
    a = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2]
    assert f(len(a) - 1) == a
