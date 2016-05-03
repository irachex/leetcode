'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        v, _ = self._find(root, k)
        return v

    def _find(self, node, k):
        cnt_left = cnt_right = 0
        if node.left:
            v, cnt_left = self._find(node.left, k)
            if v is not None:
                return v, 0
        if cnt_left + 1 == k:
            return node.val, 0
        if node.right:
            v, cnt_right = self._find(node.right, k - cnt_left - 1)
            if v is not None:
                return v, 0
        return None, cnt_left + cnt_right + 1
