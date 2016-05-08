'''
https://leetcode.com/problems/add-two-numbers/

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        head = tail = None
        r = 0
        while p1 or p2:
            p1_next = p1.next if p1 else None
            p2_next = p2.next if p2 else None
            val = (p1.val if p1 else 0) + (p2.val if p2 else 0) + r
            if val >= 10:
                val -= 10
                r = 1
            else:
                r = 0
            node = ListNode(val)
            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = node
            p1 = p1_next
            p2 = p2_next
        if r:
            node = ListNode(r)
            tail.next = node
        return head


if __name__ == '__main__':
    f = Solution().addTwoNumbers
    print f(ListNode.make_list([2, 4, 3]), ListNode.make_list([5, 6, 4]))
    print f(ListNode.make_list([2, 4, 3]), ListNode.make_list([5, 6, 9]))
    print f(ListNode.make_list([2, 4, 3]), None)
    print f(None, None)
