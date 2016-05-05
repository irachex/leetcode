'''
https://leetcode.com/problems/implement-stack-using-queues/

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
'''

from collections import deque


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        tmp_queue = deque()
        while self.queue:
            tmp_queue.append(self.queue.popleft())
        self.queue.append(x)
        while tmp_queue:
            self.queue.append(tmp_queue.popleft())

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0


if __name__ == '__main__':
    s = Stack()
    assert s.empty()
    s.push(1)
    assert s.top() == 1
    assert not s.empty()
    s.push(2)
    assert s.top() == 2
    s.push(3)
    assert s.top() == 3
    s.pop()
    assert s.top() == 2
    s.pop()
    assert s.top() == 1
