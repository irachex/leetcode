'''
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(head, k):
            p = head
            cnt = 0
            while cnt < k and p:
                cnt += 1
                p = p.next
            if cnt < k:
                return head, None, None
            last = None
            p = head
            while p and k > 0:
                k -= 1
                next = p.next
                p.next = last
                last = p
                p = next
            return last, head, p

        if k <= 1:
            return head
        result = None
        last = None
        p = head
        while p:
            new_head, new_tail, next = reverse(p, k)
            if p is head:
                result = new_head
            if last:
                last.next = new_head
            last = new_tail
            p = next
        return result


if __name__ == '__main__':
    from utils import ListNode
    f = Solution().reverseKGroup
    print f(ListNode.make_list([1, 2, 3, 4, 5]), 2)
    print f(ListNode.make_list([1, 2, 3, 4, 5]), 3)
    print f(ListNode.make_list([1, 2, 3, 4, 5]), 1)
    print f(ListNode.make_list([1, 2, 3, 4, 5]), 0)
    print f(ListNode.make_list([1, 2, 3, 4, 5]), 4)
    print f(ListNode.make_list([1, 2, 3, 4, 5]), 5)
    print f(ListNode.make_list([1, 2, 3, 4, 5]), 6)
