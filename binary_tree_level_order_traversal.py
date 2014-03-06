#coding: utf-8

'''
http://oj.leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root:
            return []
        top = 0
        layer = [root]
        result = []
        while layer:
            result.append([node.val for node in layer])
            next_layer = []
            for node in layer:
                for j in (node.left, node.right):
                    if j:
                        next_layer.append(j)
            layer = next_layer
        return result
