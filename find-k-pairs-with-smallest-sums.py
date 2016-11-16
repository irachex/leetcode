'''
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u,v) which consists of one element from the first array and one element from the second array.
Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
Return: [1,2],[1,4],[1,6]
The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2
Return: [1,1],[1,1]
The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3
Return: [1,3],[2,3]
All possible pairs are returned from the sequence:
[1,3],[2,3]
'''


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        import heapq
        h = []
        for i, x in enumerate(nums2):
            heapq.heappush(h, (nums1[0] + x, 0, i))
        result = []
        for i in xrange(k):
            if not h:
                break
            v, x, y = heapq.heappop(h)
            result.append([nums1[x], nums2[y]])
            if x + 1 < len(nums1):
                x += 1
                heapq.heappush(h, (nums1[x] + nums2[y], x, y))
        return result


if __name__ == '__main__':
    f = Solution().kSmallestPairs
    assert f([], [3,5,7,9], 1) == []
    assert f([1,7,11], [2,4,6], 3) == [[1,2],[1,4],[1,6]]
    assert f([1,1,2], [1,2,3], 2) == [[1,1],[1,1]]
    assert f([1,2], [3], 3) == [[1,3],[2,3]]
