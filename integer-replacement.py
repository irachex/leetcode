'''
https://leetcode.com/problems/integer-replacement/

Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
'''


class Solution(object):
    def integerReplacement(self, n):
        d = {1: 0}

        def find(x):
            if x in d:
                return d[x]
            if x & 1 == 0:
                v = find(x >> 1) + 1
            else:
                v = min(find(x + 1), find(x - 1)) + 1
            d[x] = v
            return v
        return find(n)

    def integerReplacement_bit(self, n):
        """
        :type n: int
        :rtype: int
        """
        def count_bits(x):
            cnt = 0
            while x:
                if x & 1:
                    cnt += 1
                x >>= 1
            return cnt

        ans = 0
        while n != 1:
            if n & 1 == 0:
                n >>= 1
            elif n == 3 or count_bits(n - 1) < count_bits(n + 1):
                n -= 1
            else:
                n += 1
            ans += 1
        return ans


if __name__ == '__main__':
    f = Solution().integerReplacement
    assert f(8) == 3
    assert f(7) == 4
    assert f(100000000) == 31
