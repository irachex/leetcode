'''
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
        # slow is head of right half now, reverse right half
        p, last = slow, None
        while p:
            next = p.next
            p.next = last
            last = p
            p = next
        # compare left half and right half
        p1, p2 = head, last
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


if __name__ == '__main__':
    from utils import ListNode
    f = Solution().isPalindrome
    assert f(ListNode.make_list([1, 2, 3, 2, 1]))
    assert f(ListNode.make_list([1, 2, 2, 1]))
    assert not f(ListNode.make_list([1, 2, 1, 1]))
    assert not f(ListNode.make_list([1, 2, 3, 1, 1]))
