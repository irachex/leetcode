#coding: utf-8

'''
http://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        top = 0
        layer = [root]
        result = []
        no = 0
        while layer:
            ilayer = reversed(layer) if len(result) & 1 else layer
            result.append([node.val for node in ilayer])
            next_layer = []
            for node in layer:
                for j in (node.left, node.right):
                    if j:
                        next_layer.append(j)
            layer = next_layer
        return result
