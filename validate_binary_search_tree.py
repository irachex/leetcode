#coding: utf-8

'''
http://oj.leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).\n\nAssume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.\nOJ's Binary Tree Serialization:\nThe serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.\n
Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if not root:
            return True
        is_valid, _, _ = self.is_valid(root)
        return is_valid

    def is_valid(self, node):
        if not node.left and not node.right:
            return True, node.val, node.val
        is_valid = True
        min_val = max_val = node.val
        if node.left:
            left_valid, left_min, left_max = self.is_valid(node.left)
            is_valid = is_valid and left_valid and left_max < node.val
            min_val = left_min
        if node.right:
            right_valid, right_min, right_max = self.is_valid(node.right)
            is_valid = is_valid and right_valid and node.val < right_min
            max_val = right_max
        return is_valid, min_val, max_val
