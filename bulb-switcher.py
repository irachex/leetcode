'''
https://leetcode.com/problems/bulb-switcher/

There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3.

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.
'''

import math

class Solution(object):

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        i = x = 0
        while i < n:
            ans += 1
            x += 2
            i += 1 + x
        return ans

    def bulbSwitch_oneline(self, n):
        return int(math.sqrt(n))

    def bulbSwitch_brute_force(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0 for i in xrange(n + 1)]
        for i in xrange(1, n + 1):
            for j in xrange(i, n + 1, i):
                a[j] = 1 - a[j]
            print a[1:]
        print '-' * 80
        return sum(a)


if __name__ == '__main__':
    f = Solution().bulbSwitch
    assert f(3) == 1
    assert f(5) == 2
    assert f(6) == 2
    assert f(7) == 2
    assert f(8) == 2
    assert f(12) == 3
    assert f(30) == 5
