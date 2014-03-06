#coding: utf-8

'''
http://oj.leetcode.com/problems/path-sum-ii/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.\n
For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
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
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if not root:
            return []
        result = []
        a = [root.val]

        def dfs(i, node, s=0):
            s += node.val
            if (not node.left and not node.right and
                    s == sum):
                result.append(a[:i])
                return
            for c in (node.left, node.right):
                if c:
                    if len(a) <= i:
                        a.append(c.val)
                    else:
                        a[i] = c.val
                    dfs(i + 1, c, s)

        dfs(1, root)
        return result


if __name__ == "__main__":
    # Definition for a  binary tree node
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    root = TreeNode(1)
    print Solution().pathSum(root, 1)

