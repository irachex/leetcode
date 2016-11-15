# coding: utf-8

'''
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 2^31.
Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
Could you do this in O(n) runtime?

Example:
Input: [3, 10, 5, 25, 2, 8]
Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in reversed(xrange(32)):
            ans <<= 1
            prefixes = {num >> i for num in nums}
            if any(ans ^ 1 ^ p in prefixes for p in prefixes):
                ans |= 1
        return ans

    def findMaximumXOR_Trie(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        class Trie(object):

            def __init__(self):
                self.edges = [None for i in xrange(2)]

            def insert(self, word):
                p = q = self
                max_xor = 0
                for x in word:
                    if not p.edges[x]:
                        p.edges[x] = Trie()

                    max_xor <<= 1
                    if q.edges[1 - x]:
                        max_xor |= 1
                        q = q.edges[1 - x]
                    else:
                        q = q.edges[x]

                    p = p.edges[x]
                return max_xor

        ans = 0
        trie = Trie()
        for n in nums:
            x = n
            binary = []
            cnt = 0
            while x:
                binary.append(x & 1)
                x >>= 1
                cnt += 1
            for i in xrange(cnt, 31):
                binary.append(0)
            ans = max(ans, trie.insert(reversed(binary)))
        return ans


if __name__ == '__main__':
    f = Solution().findMaximumXOR
    assert f([3, 10, 5, 25, 2, 8]) == 28
