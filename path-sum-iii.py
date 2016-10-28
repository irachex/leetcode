'''
https://leetcode.com/problems/path-sum-iii/

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        path = [0]
        ans = [0]

        def dfs(node, s):
            if not node:
                return
            s += node.val
            for x in path:
                if s - x == sum:
                    ans[0] += 1
            path.append(s)
            dfs(node.left, s)
            dfs(node.right, s)
            path.pop()

        dfs(root, 0)
        return ans[0]


if __name__ == '__main__':
    from utils import TreeNode
    f = Solution().pathSum
    root = TreeNode.make_tree([10,5,-3,3,2,None,11,3,-2,None,1])
    assert f(root, 8) == 3
    assert f(TreeNode.make_tree([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22) == 3
