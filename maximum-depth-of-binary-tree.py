"""
http://oj.leetcode.com/problems/maximum-depth-of-binary-tree/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        q = [(root, 1)]
        head = tail = 0
        ans = 1
        while head < len(q):
            node, dep = q[head]
            ans = max(ans, dep)
            if node.left:
                q.append((node.left, dep + 1))
            if node.right:
                q.append((node.right, dep + 1))
            head += 1
        return ans


if __name__ == "__main__":
    # Definition for a  binary tree node
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    s = Solution()

    n1 = TreeNode(0)
    n2 = TreeNode(0)
    n3 = TreeNode(0)
    n4 = TreeNode(0)
    n1.left = n2
    n2.left = n3
    n3.left = n4
    assert s.maxDepth(n1) == 4

    n1 = TreeNode(0)
    n2 = TreeNode(0)
    n3 = TreeNode(0)
    n1.left = n2
    n1.right = n3
    assert s.maxDepth(n1) == 2
