'''
https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x = self._find(nums1, nums2)
        if not x:
            x = self._find(nums2, nums1)
        return x

    def _find(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 == 0:
            return None
        if n2 == 0:
            if n1 % 2 == 1:
                return nums1[n1 / 2]
            else:
                return (nums1[n1 / 2 - 1] + nums1[n1 / 2]) / 2.0

        left1, right1 = 0, n1 - 1
        while left1 <= right1:
            mid1 = (left1 + right1) / 2
            x = nums1[mid1]

            left2, right2 = 0, n2 - 1
            lower_bound = -1 if nums2[0] >= x else 0
            while left2 <= right2:
                mid2 = (left2 + right2) / 2
                if nums2[mid2] < x:
                    lower_bound = mid2
                    left2 = mid2 + 1
                else:
                    right2 = mid2 - 1

            upper_bound = lower_bound if lower_bound >= 0 else -1
            while upper_bound + 1 < n2 and nums2[upper_bound + 1] == x:
                upper_bound += 1

            print mid1, x, lower_bound, nums2[lower_bound], upper_bound

            if (n1 + n2) % 2 == 1:
                if mid1 + upper_bound + 1 < (n1 + n2) / 2:
                    left1 = mid1 + 1
                elif mid1 + lower_bound + 1 > (n1 + n2) / 2:
                    right1 = mid1 - 1
                else:
                    return nums1[mid1]
            else:
                if mid1 + upper_bound + 1 < (n1 + n2) / 2 - 1:
                    left1 = mid1 + 1
                elif mid1 + lower_bound + 1 > (n1 + n2) / 2 - 1:
                    right1 = mid1 - 1
                else:
                    if lower_bound == -1:
                        bound = upper_bound + 1
                        if bound >= n2:
                            bound = n2 - 1
                    else:
                        bound = lower_bound + 1
                    x = nums1[mid1]
                    if (bound >= n2 or
                            mid1 + 1 < n1 and nums1[mid1 + 1] < nums2[bound]):
                        if mid1 + 1 < n1:
                            return (nums1[mid1] + nums1[mid1 + 1]) / 2.0
                        else:
                            return nums1[mid1]
                    else:
                        return (nums1[mid1] + nums2[bound]) / 2.0


if __name__ == '__main__':
    f = Solution().findMedianSortedArrays
    assert f([1, 2], [1, 1]) == 1
    assert f([1], [1]) == 1
    assert f([1], [1, 1, 1]) == 1
    assert f([1], [1, 1, 1, 5]) == 1
    assert f([1, 2], [1, 2]) == 1.5
    assert f([1, 2, 3], [1, 2, 3]) == 2
    assert f([1], [1, 1, 1, 1]) == 1
    assert f([1], [1, 1, 1]) == 1
    assert f([1], [2, 3, 4]) == 2.5
    assert f([1, 3, 5], [2, 4]) == 3
    assert f([2, 4], [1, 3, 5]) == 3
    assert f([1, 3, 5], [2, 4, 6]) == 3.5
    assert f([1, 2, 3], [4, 5, 6]) == 3.5
    assert f([1, 2, 3, 4], [5, 6]) == 3.5
    assert f([5, 6], [1, 2, 3, 4]) == 3.5
    assert f([1, 2, 3, 4], [5]) == 3
    assert f([5], [1, 2, 3, 4]) == 3
    assert f([1, 2, 3, 4, 5], []) == 3
