'''
https://leetcode.com/problems/contains-duplicate-iii/

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
'''


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):  # O(N)
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or k < 0:
            return False
        buckets = {}
        for i, x in enumerate(nums):
            key, offset = (x / t, 1) if t else (x, 0)  # t == 0 is a special case
            for bucket_key in xrange(key - offset, key + offset + 1):
                if bucket_key in buckets and abs(buckets[bucket_key] - x) <= t:
                    return True
            buckets[key] = x
            if i >= k:
                del buckets[nums[i - k] / t if t else nums[i - k]]
        return False

    def containsNearbyAlmostDuplicate_tree(self, nums, k, t):  # O(NlogK)
        if t < 0 or k < 0:
            return False
        tree = Treap()
        for i, x in enumerate(nums):
            if tree.find(x - t, x + t):
                return True
            tree.insert(x)
            if i >= k:
                tree.delete(nums[i - k])
        return False


if __name__ == '__main__':
    f = Solution().containsNearbyAlmostDuplicate
    assert not f([-3, 3], 2, 4)
    assert not f([-1,-1], 1, -1)
    assert f([-1,-1], 1, 0)
