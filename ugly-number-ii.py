'''
https://leetcode.com/problems/ugly-number-ii/

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        q = [1]
        primes = [2, 3, 5]
        p = [0, 0, 0]
        for i in xrange(1, n):
            m, j = min(((q[pj] * primes[j], j) for j, pj in enumerate(p)))
            q.append(m)
            for j, pj in enumerate(p):
                if q[pj] * primes[j] == m:
                    p[j] += 1
        return q[n - 1]


if __name__ == '__main__':
    f = Solution().nthUglyNumber
    s = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
    for i in range(1, 11):
        assert f(i) == s[i]
