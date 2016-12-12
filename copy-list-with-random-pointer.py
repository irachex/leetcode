'''
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def __repr__(self):
        return str(self.label)


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        while p:
            next = p.next
            node = RandomListNode(p.label)
            p.next = node
            node.next = next
            p = next

        p = head
        while p:
            p.next.random = p.random.next if p.random else None
            p = p.next.next

        p = head
        h = t = None
        while p:
            next = p.next.next
            if h is None:
                h = t = p.next
            else:
                t.next = p.next
                t = t.next
            p.next = next
            p = next
        return h


if __name__ == '__main__':
    f = Solution().copyRandomList

    a1 = RandomListNode(1)
    a2 = RandomListNode(2)
    a3 = RandomListNode(3)
    a1.next = a2
    a2.next = a3
    a1.random = a3
    a2.random = a1
    a3.random = a2

    y = f(a1)
    while y:
        print y, y.random, y.next
        y = y.next
