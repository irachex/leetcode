'''
https://leetcode.com/problems/count-complete-tree-nodes/

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = 0
        p = root
        exp2 = []
        m = 1
        while p:
            p = p.left
            h += 1
            exp2.append(m)
            m *= 2
        exp2.append(m)

        def check(leaves):
            p = root
            dep = 1
            while dep < h and p:
                if leaves <= exp2[h - dep - 1]:  # num of left leaves
                    p = p.left
                else:
                    leaves -= exp2[h - dep - 1]
                    p = p.right
                dep += 1
            return dep == h and p

        leaves = 0
        left, right = 1, exp2[h - 1]
        while left <= right:
            mid = (left + right) / 2
            if check(mid):
                leaves = mid
                left = mid + 1
            else:
                right = mid - 1
        return exp2[h - 1] - 1 + leaves


if __name__ == '__main__':
    f = Solution().countNodes
    nodes = [TreeNode(i) for i in xrange(7)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]
    assert f(nodes[0]) == 7

    nodes = [TreeNode(i) for i in xrange(4)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    assert f(nodes[0]) == 4

    assert f(TreeNode(0)) == 1
    assert f(None) == 0
