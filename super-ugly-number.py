# coding: utf-8

'''
https://leetcode.com/problems/super-ugly-number/

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
'''

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        q = [1]
        p = [0 for i in xrange(len(primes))]
        for i in xrange(1, n):
            m, j = min(((q[pj] * primes[j], j) for j, pj in enumerate(p)))
            q.append(m)
            for j, pj in enumerate(p):
                if q[pj] * primes[j] == m:
                    p[j] += 1
        return q[n - 1]


if __name__ == '__main__':
    f = Solution().nthSuperUglyNumber
    s = [0, 1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
    for i in range(1, 13):
        assert f(i, [2, 7, 13, 19]) == s[i]
