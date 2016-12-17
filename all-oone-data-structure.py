'''
https://leetcode.com/problems/all-oone-data-structure/

Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
'''


class Node(object):

    def __init__(self, value, next=None, prev=None, keys=None):
        self.value = value
        self.keys = set(keys or [])
        self.next = next
        self.prev = prev


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = {}  # key to node mapping
        self.head = self.tail = None  # head is min, tail is max

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        node = self.keys.get(key)
        if node is None:
            node = Node(0, keys=[key])  # dummy node with value = 0
            if self.tail is None:
                self.tail = self.head = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node

        if node.next is None or node.value + 1 < node.next.value:  # new node
            insert_node = Node(value=node.value + 1, next=node.next, prev=node)
            if node.next:
                node.next.prev = insert_node
            node.next = insert_node
            if self.tail is node:
                self.tail = insert_node
        else:
            insert_node = node.next
        insert_node.keys.add(key)
        self.keys[key] = insert_node

        node.keys.remove(key)
        if not node.keys:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if self.head is node:
                self.head = node.next
            if self.tail is node:
                self.tail = node.prev

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        node = self.keys.get(key)
        if node is None:
            return
        if node.value - 1 > 0:
            if node.prev is None or node.value - 1 > node.prev.value:  # new node
                insert_node = Node(value=node.value - 1, next=node, prev=node.prev)
                if node.prev:
                    node.prev.next = insert_node
                node.prev = insert_node
                if self.head is node:
                    self.head = insert_node
            else:
                insert_node = node.prev
            insert_node.keys.add(key)
            self.keys[key] = insert_node

        node.keys.remove(key)
        if node.value == 1:
            del self.keys[key]
        if not node.keys:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if self.head is node:
                self.head = node.next
            if self.tail is node:
                self.tail = node.prev

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return next(iter(self.tail.keys)) if self.tail else ''

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return next(iter(self.head.keys)) if self.head else ''


if __name__ == '__main__':
    a = AllOne()
    assert a.getMaxKey() == ''
    a.inc('a')
    assert a.getMaxKey() == 'a'
    a.inc('a')
    assert a.getMaxKey() == 'a'
    assert a.getMinKey() == 'a'
    a.inc('b')
    assert a.getMinKey() == 'b'
    a.dec('b')
    assert a.getMinKey() == 'a'
    assert a.getMaxKey() == 'a'
    a.inc('c')
    a.inc('c')
    a.inc('c')
    assert a.getMaxKey() == 'c'
