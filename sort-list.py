'''
https://leetcode.com/problems/sort-list/

Sort a linked list in O(n log n) time using constant space complexity.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        return self.merge_sort(head, n)

    def merge_sort(self, head, n):
        if n == 1 or head is None or head.next is None:
            return head
        # find middle
        middle = head
        for i in xrange(n / 2 - 1):
            middle = middle.next
        head2 = middle.next
        middle.next = None
        h1 = self.merge_sort(head, n / 2)
        h2 = self.merge_sort(head2, n - n / 2)
        p1, p2 = h1, h2
        h = t = None
        while p1 or p2:
            if not p2 or p1 and p1.val <= p2.val:
                if h is None:
                    h = t = p1
                else:
                    t.next = p1
                    t = p1
                p1 = p1.next
            elif not p1 or p2 and p2.val <= p1.val:
                if h is None:
                    h = t = p2
                else:
                    t.next = p2
                    t = p2
                p2 = p2.next
            else:
                break
        return h


if __name__ == '__main__':
    f = Solution().sortList
    from utils import ListNode
    print f(ListNode.make_list([3, 4, 2, 1, 7, 5, 6]))
    print f(ListNode.make_list([1]))
    print f(ListNode.make_list([5, 4, 3]))
    print f(ListNode.make_list([4,19,14,5,-3,1,8,5,11,15]))
