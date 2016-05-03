'''
https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result = []

        def dfs(p, s):
            if not p.left and not p.right:
                s += str(p.val)
                result.append(s)
                return
            s += str(p.val) + '->'
            if p.left:
                dfs(p.left, s)
            if p.right:
                dfs(p.right, s)

        if root:
            dfs(root, '')
        return result


if __name__ == '__main__':
    f = Solution().binaryTreePaths
    n = [TreeNode(i) for i in range(6)]
    n[2].right = n[5]
    n[1].left = n[2]
    n[1].right = n[3]
    print f(n[1])
