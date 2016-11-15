#coding: utf-8

'''
http://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given inorder and postorder traversal of a tree, construct the binary tree.\nNote:
You may assume that duplicates do not exist in the tree.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        root_idx = inorder.index(root.val)
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx + 1:], postorder[root_idx:-1])
        return root
