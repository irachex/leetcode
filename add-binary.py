#coding: utf-8

'''
http://oj.leetcode.com/problems/add-binary/

Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
'''

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if len(a) < len(b):
            tmp = a
            a = b
            b = tmp
        A = [0 if c == '0' else 1 for c in reversed(a)]
        B = [0 if c == '0' else 1 for c in reversed(b)]
        plus = 0
        for i in range(len(A)):
            if i < len(B):
                A[i] += B[i] + plus
            else:
                A[i] += plus
            if A[i] >= 2:
                A[i] -= 2
                plus = 1
            else:
                plus = 0
        if plus:
            A.append(plus)
        return ''.join(map(str, reversed(A)))


if __name__ == "__main__":
    assert Solution().addBinary('11', '1') == '100'
