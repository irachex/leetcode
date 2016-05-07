'''
https://leetcode.com/problems/recover-binary-search-tree/

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        wrong = []
        last = [None]

        def check(p):
            # print p.val
            if last[0] and last[0].val > p.val:
                wrong.append(last[0])
                wrong.append(p)
            last[0] = p

        def inorder_morris_traversal(root):
            p = root
            prev = None
            while p:
                if p.left is None:
                    check(p)
                    p = p.right
                else:
                    prev = p.left
                    while prev.right and prev.right is not p:
                        prev = prev.right

                    if prev.right is None:
                        prev.right = p
                        p = p.left
                    else:
                        prev.right = None
                        check(p)
                        p = p.right

        inorder_morris_traversal(root)

        w1 = w2 = None
        if len(wrong) == 2:
            w1, w2 = wrong
        else:  # len(wrong) == 4
            # w[0] > w[1]       w[2] > w[3]
            w1, w2 = wrong[0], wrong[3]

        tmp = w1.val
        w1.val = w2.val
        w2.val = tmp
        return root


if __name__ == '__main__':
    f = Solution().recoverTree
    x = TreeNode(0)
    y = TreeNode(1)
    x.left = y
    f(x)

    n1 = TreeNode(2)
    n2 = TreeNode(1)
    n1.right = n2
    f(n1)
