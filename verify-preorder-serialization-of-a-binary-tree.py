'''
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false
'''

class Solution(object):
    def isValidSerialization(self, preorder):
        slot = 1
        for c in preorder.split(','):
            if slot == 0:
                return False
            if c != '#':
                slot += 2
            slot -= 1
        return slot == 0

    def isValidSerialization_stack(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        preorder = preorder.split(',')
        for i, c in enumerate(preorder):
            if c != '#':
                stack.append([c, 0])
            else:
                stack.append([c, 2])
            while stack and stack[-1][1] == 2:
                stack.pop()
                if stack:
                    stack[-1][1] += 1
            if i < len(preorder) - 1 and not stack:
                return False
        return not stack


if __name__ == '__main__':
    f = Solution().isValidSerialization
    assert f("9,3,4,#,#,1,#,#,2,#,6,#,#")
    assert not f('')
    assert f('#')
    assert not f('1,#')
    assert not f('9,#,#,1')
