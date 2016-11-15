#coding: utf-8

'''
http://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.\n
For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return head
        new_head = head.__class__(0)
        new_head.next = head
        pre_last = new_head
        last = head
        current = head.next
        last_delete = None
        while current:
            if current.val == last.val:
                pre_last.next = current.next
                last_delete = current.val
            else:
                if last_delete != last.val:
                    pre_last = last
                last = current
            current = current.next
        return new_head.next


if __name__ == "__main__":
    from utils import ListNode
    head = ListNode.make_list([1, 1, 2, 2])
    p = Solution().deleteDuplicates(head)
    print p
