# coding: utf-8

'''
https://leetcode.com/problems/permutation-sequence/

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        a = [i for i in xrange(1, n + 1)]
        f = [1 for i in xrange(n)]
        for i in xrange(1, n):
            f[i] = f[i - 1] * i

        k -= 1
        p = []
        while n > 0:
            x = a[k / f[n - 1]]
            p.append(x)
            a.remove(x)
            k = k % f[n - 1]
            n -= 1
        return ''.join(map(str, p))


if __name__ == '__main__':
    f = Solution().getPermutation
    assert f(1, 1) == '1'
    assert f(3, 1) == '123'
    assert f(3, 2) == '132'
    assert f(3, 3) == '213'
    assert f(3, 4) == '231'
    assert f(3, 5) == '312'
    assert f(3, 6) == '321'
