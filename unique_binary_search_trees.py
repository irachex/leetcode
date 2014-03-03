"""
http://oj.leetcode.com/problems/unique-binary-search-trees/

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution:
    # @return an integer
    def numTrees(self, n):
        d = [0 for i in range(n + 1)]
        d[0] = 1
        for i in range(1, n + 1):
            d[i] = sum(d[j] * d[i - 1 - j] for j in range(0, i))
        return d[n]


if __name__ == "__main__":
    s = Solution()
    assert s.numTrees(3) == 5
