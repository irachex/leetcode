"""
http://oj.leetcode.com/problems/remove-element/

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        cnt = 0
        n = len(A)
        for i in range(n):
            if A[i] == elem:
                cnt += 1
            elif cnt and i - cnt >= 0:
                A[i - cnt] = A[i]
        del A[n - cnt:]
        return n - cnt


if __name__ == "__main__":
    s = Solution()
    a = [4, 5]
    s.removeElement(a, 4)
    assert a == [5]

    b = [4, 5]
    s.removeElement(b, 5)
    assert b == [4]
