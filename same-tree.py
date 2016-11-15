"""
http://oj.leetcode.com/problems/same-tree/

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if not (p and q and p.val == q.val):
            return False
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


if __name__ == "__main__":
    # Definition for a  binary tree node
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    s = Solution()

    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a1.left = a2
    a2.right = a3

    b1 = TreeNode(1)
    b2 = TreeNode(2)
    b3 = TreeNode(3)
    b1.left = b2
    b2.right = b3

    c1 = TreeNode(1)
    c2 = TreeNode(2)
    c3 = TreeNode(4)
    c1.left = c2
    c2.right = c3

    assert s.isSameTree(a1, b1)
    assert not s.isSameTree(a1, c1)
