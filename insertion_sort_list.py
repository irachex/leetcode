#coding: utf-8

'''
http://oj.leetcode.com/problems/insertion-sort-list/

Sort a linked list using insertion sort.
'''

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        p = head
        new_head = head.__class__(0)
        tail = None
        while p:
            print p.val
            node = p.__class__(p.val)
            if tail and node.val > tail.val:
                tail = self.insert(tail, tail, node)
            else:
                tail = self.insert(new_head, tail, node)
            p = p.next
        return new_head.next

    def insert(self, head, tail, node):
        current = head.next
        last = head
        while current:
            if current.val > node.val:
                break
            last = current
            current = current.next
        if last:
            last.next = node
        node.next = current
        return node if current is None else tail


if __name__ == "__main__":
    from utils import ListNode
    head = ListNode.make_list([3, 2, 1])
    p = Solution().insertionSortList(head)
    print p.to_list()
