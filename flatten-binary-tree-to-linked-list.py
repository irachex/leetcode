#coding: utf-8

'''
http://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given a binary tree, flatten it to a linked list in-place.
For example,
Given
         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.
Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return root

        def dfs(node):
            if not node:
                return None, None
            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)

            node.left = None
            node.right = left_min or right_min
            if left_max:
                left_max.right = right_min

            return node, right_max or left_max or node

        dfs(root)


if __name__ == "__main__":
    from utils import TreeNode
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3

    Solution().flatten(n1)

    assert n1.right is n2
    assert n1.left is None
    assert n2.left is None
    assert n2.right is n3
    assert n3.left is None and n3.right is None
