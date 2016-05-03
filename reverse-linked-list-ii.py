# coding: utf-8

'''
https://leetcode.com/problems/reverse-linked-list-ii/

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        i = 1
        p = head
        last = None
        while i < m:
            last = p
            p = p.next
            i += 1
        rhead = p
        rlast = None
        while p and i <= n:
            next = p.next
            p.next = rlast
            rlast = p
            p = next
            i += 1
        rhead.next = p
        if m > 1:
            last.next = rlast
        else:
            head = rlast
        return head


if __name__ == '__main__':
    from utils import ListNode
    f = Solution().reverseBetween
    print f(ListNode.make_list([1, 2, 3, 4, 5]), 2, 4)
    print f(ListNode.make_list([1, 2, 3, 4, 5]), 2, 5)
    print f(ListNode.make_list([1, 2, 3, 4, 5]), 1, 5)
    print f(ListNode.make_list([1, 2, 3, 4, 5]), 1, 4)
