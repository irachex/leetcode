#coding: utf-8

'''
http://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?
For example,
Given sorted array A = [1,1,1,2,2,3],
Your function should return length = 5, and A is now [1,1,2,2,3].
'''

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        current = None
        cnt = 0
        ans = 0
        for i, x in enumerate(A, 1):
            if i > 0 and x == current:
                cnt += 1
                if cnt <= 2:
                    A[ans] = x
                    ans += 1
            else:
                cnt = 1
                current = x
                A[ans] = x
                ans += 1
        A = A[:ans]
        return ans


if __name__ == "__main__":
    A = [1, 1, 1, 2, 2, 3]
    print Solution().removeDuplicates(A), A
