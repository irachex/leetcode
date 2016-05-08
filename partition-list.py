'''
https://leetcode.com/problems/partition-list/

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        p = head
        less_head = less_tail = None
        greater_head = greater_tail = None
        while p:
            if p.val < x:
                if less_head is None:
                    less_head = less_tail = p
                else:
                    less_tail.next = p
                    less_tail = p
            else:
                if greater_head is None:
                    greater_head = greater_tail = p
                else:
                    greater_tail.next = p
                    greater_tail = p
            p = p.next
        if greater_tail:
            greater_tail.next = None
        if less_tail:
            less_tail.next = greater_head
        return less_head or greater_head


if __name__ == '__main__':
    f = Solution().partition
    from utils import ListNode
    print f(ListNode.make_list([1, 4, 3, 2, 5, 2]), 3)
    print f(ListNode.make_list([1]), 0)
