#coding: utf-8

'''
http://oj.leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
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
    def isBalanced(self, root):
        is_balance, _ = self.is_balance(root)
        return is_balance

    def is_balance(self, node):
        if node is None:
            return True, 0
        left_balance, left_dep = self.is_balance(node.left)
        right_balance, right_dep = self.is_balance(node.right)
        is_balance = (left_balance and
                      right_balance and
                      abs(left_dep - right_dep) <= 1)
        return is_balance, max(left_dep, right_dep) + 1
