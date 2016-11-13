'''
https://leetcode.com/problems/elimination-game/

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.
We keep repeating the steps again, alternating left to right and right to left, until a single number remains.
Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
'''


class Solution(object):

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        step = 2
        num = n
        while num > 1:
            if step > 0:
                start += step / 2
            else:
                if num & 1:
                    start -= step / 2
            step = -step * 2
            num >>= 1
        return start


if __name__ == '__main__':
    f = Solution().lastRemaining
    for i in xrange(1, 10):
        print i, f(i)
    assert f(9) == 6
