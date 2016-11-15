#coding: utf-8

'''
http://oj.leetcode.com/problems/binary-tree-maximum-path-sum/

Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree.
For example:
Given the below binary tree,
       1
      / \
     2   3
Return 6.
'''

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        ans = [-99999999]

        def dfs(node):
            if not node:
                return 0
            max_left = dfs(node.left)
            max_right = dfs(node.right)
            max_self = max(node.val,
                           node.val + max_left,
                           node.val + max_right)
            ans[0] = max(ans[0], max_self, node.val + max_left + max_right)
            return max_self

        dfs(root)

        return ans[0]


if __name__ == "__main__":
    from utils import TreeNode
    root = TreeNode(0)
    assert Solution().maxPathSum(root) == 0

    root = TreeNode(-3)
    assert Solution().maxPathSum(root) == -3
