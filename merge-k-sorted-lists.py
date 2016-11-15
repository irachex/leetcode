#coding: utf-8

'''
http://oj.leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        lists = filter(None, lists)
        if not lists:
            return None
        head = lists[0].__class__(0)
        node = head
        while len(lists) > 1:
            lists.sort(key=lambda n: n.val)
            node.next = lists[0]
            lists[0] = lists[0].next
            if lists[0] is None:
                lists = lists[1:]
            node = node.next
        if lists:
            node.next = lists[0]
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
    p = s.mergeKLists([n1, n2])
    assert p.val == 0

    n1 = ListNode(1)
    n2 = ListNode(1)
    p = s.mergeKLists([n1, n2])
    assert p.val == 1
    assert p.next.val == 1

    n1 = ListNode(1)
    n3 = ListNode(3)
    n1.next = n3

    n2 = ListNode(2)
    n4 = ListNode(4)
    n2.next = n4

    p = s.mergeKLists([n1, n2])
    assert p.val == 1
    assert p.next.val == 2
    assert p.next.next.val == 3
    assert p.next.next.next.val == 4
