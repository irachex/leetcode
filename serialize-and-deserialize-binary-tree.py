'''
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(p):
            if not p:
                return '#'
            return '(' + str(p.val) + ',' + dfs(p.left) + ',' + dfs(p.right) + ')'

        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(s):
            if not s or s[0] == '#':
                return None
            if s[0] == '(':
                return dfs(s[1:-1])
            b = 0
            q = []
            for i, c in enumerate(s):
                if c == ',':
                    if b == 0:
                        q.append(i)
                elif c == '(':
                    b += 1
                elif c == ')':
                    b -= 1
            p = TreeNode(int(s[:q[0]]))
            p.left = dfs(s[q[0] + 1:q[1]])
            p.right = dfs(s[q[1] + 1:len(s)])
            return p

        return dfs(data)


if __name__ == '__main__':
    codec = Codec()
    nodes = [TreeNode(i) for i in range(5)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    root = nodes[0]
    print codec.serialize(root)
    codec.deserialize(codec.serialize(root))
    print codec.serialize(codec.deserialize(codec.serialize(root)))
    codec.deserialize(codec.serialize(None))
