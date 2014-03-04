#coding: utf-8

'''
http://oj.leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not (l1 or l2):
            return None
        head = (l1 or l2).__class__(0)
        node = head
        while l1 or l2:
            if l1 and (not l2 or l1.val < l2.val):
                node.next = l1
                l1 = l1.next
            elif l2 and (not l1 or l2.val <= l1.val):
                node.next = l2
                l2 = l2.next
            else:
                break
            node = node.next
        return head.next


if __name__ == "__main__":
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    s = Solution()

    n1 = None
    n2 = ListNode(0)
    p = s.mergeTwoLists(n1, n2)
    assert p.val == 0

    n1 = ListNode(1)
    n2 = ListNode(1)
    p = s.mergeTwoLists(n1, n2)
    assert p.val == 1
    assert p.next.val == 1

    n1 = ListNode(1)
    n3 = ListNode(3)
    n1.next = n3

    n2 = ListNode(2)
    n4 = ListNode(4)
    n2.next = n4

    p = s.mergeTwoLists(n1, n2)
    assert p.val == 1
    assert p.next.val == 2
    assert p.next.next.val == 3
    assert p.next.next.next.val == 4
