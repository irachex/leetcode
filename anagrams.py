'''
https://leetcode.com/problems/anagrams/

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
'''

from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for w in strs:
            d[''.join(sorted(w))].append(w)
        return [sorted(v) for v in d.itervalues()]


if __name__ == '__main__':
    f = Solution().groupAnagrams
    print f(["eat", "tea", "tan", "ate", "nat", "bat"])
