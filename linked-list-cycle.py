"""
http://oj.leetcode.com/problems/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        """
        require O(1) space
        fast runner move 2 steps at one time while slow runner move 1 step,
        if traverse to a null, there must be no loop
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle_sol2(self, head):
        """
        require O(n) space
        """
        while head:
            if getattr(head, 'is_visited', False):
                return True
            head.is_visited = True
            head = head.next
        return False


if __name__ == "__main__":
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    s = Solution()

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    c.next = b
    assert s.hasCycle(a)

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    assert not s.hasCycle(a)
