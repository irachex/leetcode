#coding: utf-8

'''
http://oj.leetcode.com/problems/3sum/

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.\nNote:Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        n = len(num)

        result = []
        for i in range(n - 2):
            if i > 0 and num[i] == num[i - 1]:
                continue
            a = num[i]
            j = i + 1
            k = n - 1
            while j < k:
                s = a + num[j] + num[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    result.append([a, num[j], num[k]])
                    j += 1
                    k -= 1
                    while j < k and num[j] == num[j - 1]:
                        j += 1
                    while k > j and num[k] == num[k + 1]:
                        k -= 1

        return result


if __name__ == "__main__":
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1, -4])
    print s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
