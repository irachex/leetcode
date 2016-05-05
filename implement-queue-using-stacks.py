'''
https://leetcode.com/problems/implement-queue-using-stacks/

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        tmp_stack = []
        while self.stack:
            tmp_stack.append(self.stack.pop())
        self.stack.append(x)
        while tmp_stack:
            self.stack.append(tmp_stack.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0


if __name__ == '__main__':
    q = Queue()
    assert q.empty()
    q.push(1)
    assert q.peek() == 1
    assert not q.empty()
    q.push(2)
    assert q.peek() == 1
    q.push(3)
    q.pop()
    assert q.peek() == 2
    q.pop()
    assert q.peek() == 3
