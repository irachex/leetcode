'''
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        last = None
        while p:
            next = p.next
            p.next = last
            last = p
            p = next
        return last
