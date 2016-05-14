'''
https://leetcode.com/problems/odd-even-linked-list/

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import ListNode


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h1 = t1 = ListNode(None)
        h2 = t2 = ListNode(None)
        p = head
        while p:
            t1.next = p
            t1 = p
            p = p.next
            if p:
                t2.next = p
                t2 = p
                p = p.next
        t2.next = None
        t1.next = h2.next
        return h1.next


if __name__ == '__main__':
    f = Solution().oddEvenList
    head = ListNode.make_list([1, 2, 3, 4, 5])
    print f(head)
    print f(None)
