#coding: utf-8

'''
http://oj.leetcode.com/problems/permutations/

Given a collection of numbers, return all possible permutations.
For example,[1,2,3] have the following permutations:[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        b = [False for x in num]
        a = [0 for x in num]
        result = []

        def generate(i):
            if i == len(num):
                result.append(a[:])
            for j, x in enumerate(num):
                if not b[j]:
                    b[j] = True
                    a[i] = x
                    generate(i + 1)
                    b[j] = False

        generate(0)
        return result


if __name__ == '__main__':
    print Solution().permute([1, 2, 3])
