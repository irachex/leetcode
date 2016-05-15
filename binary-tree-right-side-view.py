'''
https://leetcode.com/problems/binary-tree-right-side-view/

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        layer = [root]
        result = []
        while layer:
            result.append(layer[-1].val)
            next_layer = []
            for node in layer:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            layer = next_layer
        return result


if __name__ == '__main__':
    f = Solution().rightSideView
    nodes = [None] + [TreeNode(i) for i in xrange(1, 7)]
    nodes[1].left = nodes[2]
    nodes[2].right = nodes[5]
    nodes[1].right = nodes[3]
    nodes[3].right = nodes[4]
    assert f(nodes[1]) == [1, 3, 4]
