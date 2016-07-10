'''
https://leetcode.com/problems/super-pow/

Your task is to calculate a^b mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024
'''


def my_pow(a, b, m):
    r = 1
    p = a
    while b:
        if b & 1:
            r = (r * p) % m
        b >>= 1
        p = (p * p) % m
    return r


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        m = 1337
        r = 1
        pa = a
        for x in reversed(b):
            r = (r * my_pow(pa, x, m)) % m
            pa = my_pow(pa, 10, m)
        return r


if __name__ == '__main__':
    f = Solution().superPow
    assert my_pow(2, 3, 1337) == 8
    assert my_pow(2, 10, 1337) == 1024
    assert f(2, [3]) == 8
    assert f(2, [1, 0]) == 1024
