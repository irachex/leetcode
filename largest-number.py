'''
https://leetcode.com/problems/largest-number/

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def _cmp(x, y):
            i = 0
            n = len(x)
            m = len(y)
            while i < n and i < m:
                if x[i] < y[i]:
                    return -1
                elif x[i] > y[i]:
                    return 1
                i += 1
            if i >= n and i < m:
                return _cmp(x, y[i:])
            if i >= m and i < n:
                return _cmp(x[i:], y)
            return 0

        if all(x == 0 for x in nums):
            return '0'

        return ''.join(sorted([str(x) for x in nums], cmp=_cmp, reverse=True))

    def largestNumber_one_line(self, nums):
        return ''.join(sorted([str(x) for x in nums], cmp=lambda x, y: cmp(y + x, x + y))) if any(x for x in nums) else '0'


if __name__ == '__main__':
    f = Solution().largestNumber
    assert f([121, 12]) == '12121'
    assert f([3, 30, 34, 5, 9]) == '9534330'
    assert f([0, 0]) == '0'
