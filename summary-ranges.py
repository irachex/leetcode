'''
https://leetcode.com/problems/summary-ranges/

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        result = []
        start = end = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] == end + 1:
                end += 1
            else:
                s = '%s->%s' % (start, end) if start < end else str(end)
                result.append(s)
                start = end = nums[i]
        s = '%s->%s' % (start, end) if start < end else str(end)
        result.append(s)
        return result


if __name__ == '__main__':
    f = Solution().summaryRanges
    assert f([0,1,2,4,5,7]) == ["0->2","4->5","7"]
    assert f([0]) == ['0']
    assert f([0, 1]) == ['0->1']
    assert f([]) == []
