# coding: utf-8

'''
https://leetcode.com/problems/reorder-list/

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        p = head
        n = 0
        while p:
            p = p.next
            n += 1

        # find middle
        middle = head
        for i in xrange(n / 2):
            middle = middle.next

        # reverse middle
        last = None
        p = middle
        while p:
            next = p.next
            p.next = last
            last = p
            p = next

        # merge head and last
        p1, p2 = head, last
        while p1 or p2:
            p1_next = p1.next if p1 else None
            p2_next = p2.next if p2 else None
            if p1:
                p1.next = p2
            if p2:
                p2.next = p1_next
            p1 = p1_next
            p2 = p2_next


if __name__ == '__main__':
    f = Solution().reorderList
    from utils import ListNode
    head = ListNode.make_list([1, 2, 3, 4])
    f(head)
    print head
    head = ListNode.make_list([1, 2, 3, 4, 5])
    f(head)
    print head
    f(None)
