#coding: utf-8

'''
http://oj.leetcode.com/problems/sum-root-to-leaf-numbers/

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
For example,
    1
   / \
  2   3
  The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Return the sum = 12 + 13 = 25.
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
    def sumNumbers(self, root):
        if not root:
            return 0
        s = [0]

        def dfs(node, x):
            if not node.left and not node.right:
                s[0] += x
                return
            for c in (node.left, node.right):
                if c:
                    dfs(c, x * 10 + c.val)

        dfs(root, root.val)

        return s[0]
