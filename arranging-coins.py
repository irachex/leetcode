# coding: utf-8

'''
https://www.douban.com/location/people/irachex/events/wish

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
'''

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n >= cnt + 1:
            cnt += 1
            n -= cnt
        return cnt


if __name__ == '__main__':
    f = Solution().arrangeCoins
    assert f(5) == 2
    assert f(8) == 3
