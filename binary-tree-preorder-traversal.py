"""
http://oj.leetcode.com/problems/binary-tree-preorder-traversal/

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root is None:
            return []
        result = []
        stack = [root]
        root.next = 0

        while stack:
            node = stack[-1]
            if node.next == 0:
                result.append(node.val)
                node.next += 1
                if node.left:
                    node.left.next = 0
                    stack.append(node.left)
            elif node.next == 1:
                node.next += 1
                if node.right:
                    node.right.next = 0
                    stack.append(node.right)
            else:
                stack.pop()

        return result


if __name__ == "__main__":
    # Definition for a  binary tree node
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

        def __repr__(self):
            return str(self.val)

    s = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3

    assert s.preorderTraversal(n1) == [1, 2, 3]
