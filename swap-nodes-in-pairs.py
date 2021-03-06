#coding: utf-8

'''
http://oj.leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return head
        p1 = head
        p2 = head.next
        last = None
        new_head = p2 if p2 else p1
        while p1 and p2:
            p = p2.next
            p1.next = p
            p2.next = p1
            if last:
                last.next = p2
            last = p1
            p1 = p
            p2 = p1.next if p1 else None
        return new_head
