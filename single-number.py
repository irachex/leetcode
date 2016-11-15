"""
http://oj.leetcode.com/problems/single-number/

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for x in A:
            ans ^= x
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.singleNumber([1, 1, 2]) == 2
    assert s.singleNumber([1, 1, 2, 2, 3]) == 3
