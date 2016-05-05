'''
https://leetcode.com/problems/remove-linked-list-elements/

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = head
        while p and p.val == val:
            p = p.next
        head = p
        last = None
        while p:
            if p.val == val:
                last.next = p.next
            else:
                last = p
            p = p.next
        return head


if __name__ == '__main__':
    f = Solution().removeElements
    from utils import ListNode
    print f(ListNode.make_list([1, 2, 6, 3, 4, 5, 6]), 6)
    print f(ListNode.make_list([6, 6, 1, 2, 6, 3, 4, 5, 6]), 6)
    print f(ListNode.make_list([1, 2, 2, 1]), 2)
