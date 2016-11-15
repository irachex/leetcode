#coding: utf-8

'''
http://oj.leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.\nThe minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 99999999
            if not node.left and not node.right:
                return 1
            return min(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)
