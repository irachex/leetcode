'''
https://leetcode.com/problems/rotate-list/

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        n = 0
        p = head
        tail = p
        while p:
            tail = p
            p = p.next
            n += 1
        tail.next = head
        k = k % n
        for i in xrange(n - k):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head


if __name__ == '__main__':
    f = Solution().rotateRight
    from utils import ListNode
    head = ListNode.make_list([1, 2, 3, 4, 5])
    print f(head, 2)
