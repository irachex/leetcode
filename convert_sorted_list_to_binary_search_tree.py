#coding: utf-8

'''
http://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return self.build_tree(a, 0, len(a) - 1)

    def build_tree(self, a, left, right):
        if left > right:
            return None
        mid = (left + right) / 2
        node = TreeNode(a[mid])
        if left == right:
            return node
        node.left = self.build_tree(a, left, mid - 1)
        node.right = self.build_tree(a, mid + 1, right)
        return node
