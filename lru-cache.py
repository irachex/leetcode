'''
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
'''


class Node(object):

    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoubleLinkedQueue(object):

    def __init__(self):
        self.head = self.tail = None

    def pop(self):
        if self.head is None:
            return
        node = self.head
        self.delete(self.head)
        return node

    def push(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        return node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        elif self.head:
            self.head = self.head.next
        else:
            raise
        if node.next:
            node.next.prev = node.prev
        elif self.tail:
            self.tail = self.tail.prev
        else:
            raise

    def __str__(self):
        a = []
        p = self.head
        while p is not None:
            a.append(p.value)
            p = p.next
        return '->'.join(map(str, a))


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self._data = {}
        self._node_map = {}
        self._queue = DoubleLinkedQueue()

    def get(self, key):
        """
        :rtype: int
        """
        v = self._data.get(key, -1)
        if v != -1:
            self._touch(key)
        return v

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        self._data[key] = value
        self._touch(key)

        if len(self._data) > self.capacity:
            self._invalidate()

    def _touch(self, key):
        node = self._node_map.get(key)
        if node is not None:
            self._queue.delete(node)
        self._node_map[key] = self._queue.push(key)

    def _invalidate(self):
        node = self._queue.pop()
        del self._data[node.value]
        del self._node_map[node.value]


def solve(capacity, ops):
    c = LRUCache(capacity)
    result = []
    for op in ops:
        print op
        v = eval('c.' + op)
        if op.startswith('get'):
            result.append(v)
        print c._queue
    return result


if __name__ == '__main__':
    assert solve(1,['set(2,1)','get(2)','set(3,2)','get(2)','get(3)']) == [1,-1,2]
    print '=' * 20
    assert solve(2,['get(2)','set(2,6)','get(1)','set(1,5)','set(1,2)','get(1)','get(2)']) == [-1, -1, 2, 6]

    c = LRUCache(3)
    c.set('a', 1)
    c.set('b', 2)
    c.set('c', 3)
    assert c.get('a') == 1 and c.get('b') == 2 and c.get('c') == 3
    assert c.get('d') == -1
    c.set('d', 4)
    assert c.get('d') == 4
    assert c.get('a') == -1 and c.get('b') == 2 and c.get('c') == 3
