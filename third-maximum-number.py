'''
https://leetcode.com/problems/third-maximum-number/

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MIN = -(1 << 63)
        m1 = m2 = m3 = MIN
        for x in nums:
            if m1 < x:
                m3 = m2
                m2 = m1
                m1 = x
            elif m2 < x and x < m1:
                m3 = m2
                m2 = x
            elif m3 < x and x < m2:
                m3 = x
        return m3 if m3 > MIN else m1


if __name__ == '__main__':
    f = Solution().thirdMax
    assert f([3, 2, 1]) == 1
    assert f([1, 2]) == 2
    assert f([2, 2, 3, 1]) == 1
    print f([5, 5, 3, 1, 1, 0])
    print f([1,2,-2147483648])
