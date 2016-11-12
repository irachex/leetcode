'''
https://leetcode.com/problems/intersection-of-two-arrays/

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

    def intersection_sort(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        result = []
        j = 0
        for i, x in enumerate(nums1):
            if i > 0 and x == nums1[i - 1]:
                continue
            while j < len(nums2) and nums2[j] < x:
                j += 1
            if j < len(nums2) and nums2[j] == x:
                result.append(x)
        return result


if __name__ == '__main__':
    f = Solution().intersection_sort
    assert f([1, 2, 2, 1], [2, 2]) == [2]
    assert f([1, 2, 3, 4, 5], [3, 3, 4, 7, 8]) == [3, 4]
    assert f([3, 4, 7, 8], [1, 2, 3, 4, 5]) == [3, 4]
