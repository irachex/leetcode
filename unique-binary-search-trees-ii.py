'''
https://leetcode.com/problems/unique-binary-search-trees-ii/

Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self._gen(1, n)

    def _gen(self, p, q):
        if p == q:
            return [TreeNode(p)]
        result = []
        for i in xrange(p, q + 1):
            ltrees = self._gen(p, i - 1) if p <= i - 1 else [None]
            rtrees = self._gen(i + 1, q) if i + 1 <= q else [None]
            for ltree in ltrees:
                for rtree in rtrees:
                    root = TreeNode(i)
                    root.left = ltree
                    root.right = rtree
                    result.append(root)
        return result


if __name__ == '__main__':
    f = Solution().generateTrees
    print f(3)
