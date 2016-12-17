'''
https://leetcode.com/problems/maximum-gap/

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
'''


class Solution(object):
    def maximumGap(self, nums):  # bucket, pigeon hole principle
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        max_value = max(nums)
        min_value = min(nums)
        # remove max_value and min_value, there are at most n - 2 numbers left
        # if we have n - 1 bucket, then there must be an empty bucket.
        bucket_size = n - 1
        interval = (max_value - min_value) / float(bucket_size)
        MAX_INT, MIN_INT = 1 << 40, -(1 << 40)
        bucket_max = [MIN_INT for i in xrange(bucket_size)]
        bucket_min = [MAX_INT for i in xrange(bucket_size)]
        for x in nums:
            if x == max_value or x == min_value:
                continue
            idx = int((x - min_value) / interval)
            bucket_max[idx] = max(bucket_max[idx], x)
            bucket_min[idx] = min(bucket_min[idx], x)

        ans = 0
        prev_max = min_value
        for i in xrange(bucket_size):
            if bucket_max[i] == MIN_INT:  # empty bucket
                continue
            ans = max(ans, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
        ans = max(ans, max_value - prev_max)
        return ans

    def maximumGap_radix_sort(self, nums):  # Accpeted. But it can't deal with negative number
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        a = radix_sort(nums)
        return max(a[i] - a[i - 1] for i in xrange(1, n))


def radix_sort(a):
    def counting_sort(a, exp):
        count = [0 for i in xrange(base)]
        for x in a:
            count[x / exp % base] += 1
        for i in xrange(1, base):
            count[i] += count[i - 1]
        result = [0 for i in xrange(len(a))]
        for x in reversed(a):
            digit = x / exp % base
            result[count[digit] - 1] = x
            count[digit] -= 1
        return result

    max_value = max(a)
    exp = 1
    base = 10
    while exp <= max_value:
        a = counting_sort(a, exp)
        exp *= base
    return a


if __name__ == '__main__':
    f = Solution().maximumGap
    assert f([3, 6, 9, 1]) == 3
    assert f([]) == 0
    assert f([17, 4, 7, 9, 80, 2, 1, 6]) == 63
