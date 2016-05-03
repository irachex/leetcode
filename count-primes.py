'''
https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = [True for i in xrange(n)]
        ans = 0
        for i in xrange(2, n):
            if b[i]:
                ans += 1
                for j in xrange(i * i, n, i):
                    b[j] = False
        return ans


if __name__ == '__main__':
    f = Solution().countPrimes
    assert f(10) == 4
    assert f(12) == 5
    assert f(18) == 7
