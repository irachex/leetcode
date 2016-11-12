'''
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        result = []
        j = 0
        for i, x in enumerate(nums1):
            while j < len(nums2) and nums2[j] < x:
                j += 1
            if j < len(nums2) and nums2[j] == x:
                j += 1
                result.append(x)
        return result


if __name__ == '__main__':
    f = Solution().intersect
    assert f([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert f([1, 2, 3, 4, 5], [3, 3, 4, 7, 8]) == [3, 4]
    assert f([3, 4, 7, 8], [1, 2, 3, 4, 5]) == [3, 4]
    assert f([1, 2, 3, 4, 3, 5], [3, 3, 4, 7, 8]) == [3, 3, 4]
