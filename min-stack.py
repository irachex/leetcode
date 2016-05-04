'''
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._top = -1
        self._stack = []
        self._min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._top += 1
        min_v = min(x, self._min_stack[self._top - 1]) if self._top > 0 else x
        if len(self._stack) < self._top + 1:
            self._stack.append(x)
            self._min_stack.append(min_v)
        else:
            self._stack[self._top] = x
            self._min_stack[self._top] = min_v

    def pop(self):
        """
        :rtype: void
        """
        x = self._stack[self._top]
        self._top -= 1
        return x

    def top(self):
        """
        :rtype: int
        """
        return self._stack[self._top]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min_stack[self._top]


if __name__ == '__main__':
    s = MinStack()
    s.push(5)
    assert s.getMin() == 5
    s.push(3)
    assert s.getMin() == 3
    assert s.top() == 3
    s.pop()
    assert s.getMin() == 5
    assert s.top() == 5
