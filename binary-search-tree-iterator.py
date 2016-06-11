'''
https://leetcode.com/problems/binary-search-tree-iterator/

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        p = root
        while p:
            self.stack.append(p)
            p = p.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        if node.right:
            p = node.right
            while p:
                self.stack.append(p)
                p = p.left
        return node.val


if __name__ == '__main__':
    nodes = [TreeNode(i) for i in xrange(4)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    root = nodes[0]
    it = BSTIterator(root)
    while it.hasNext():
        print it.next()
