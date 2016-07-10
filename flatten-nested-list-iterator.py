'''
https://leetcode.com/problems/flatten-nested-list-iterator/

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):

    def __init__(self, v):
        self.v = v

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return not isinstance(self.v, list)

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.v

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.v

    @classmethod
    def make_list(cls, data):
        r = []
        for v in data:
            if isinstance(v, list):
                r.append(cls(cls.make_list(v)))
            else:
                r.append(cls(v))
        return r

    def __repr__(self):
        return str(self.v)


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.it = self.iter(nestedList)
        self.next_value = next(self.it, None)

    def iter(self, nestedList):
        stack = [[nestedList, 0]]
        top = 0
        while top >= 0:
            t, p = stack[top]
            if p < len(t):
                x = t[p]
                stack[top][1] += 1
                if x.isInteger():
                    yield x.getInteger()
                else:
                    top += 1
                    if top >= len(stack):
                        stack.append([x.getList(), 0])
                    else:
                        stack[top] = [x.getList(), 0]
            else:
                top -= 1

    def next(self):
        """
        :rtype: int
        """
        x = self.next_value
        self.next_value = next(self.it, None)
        return x

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_value is not None


class NestedIterator2(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]
        self.top = 0
        self.next_value = self._next()

    def _next(self):
        while self.top >= 0:
            t, p = self.stack[self.top]
            if p < len(t):
                x = t[p]
                self.stack[self.top][1] += 1
                if x.isInteger():
                    return x.getInteger()
                else:
                    self.top += 1
                    if self.top >= len(self.stack):
                        self.stack.append([x.getList(), 0])
                    else:
                        self.stack[self.top] = [x.getList(), 0]
            else:
                self.top -= 1

    def next(self):
        """
        :rtype: int
        """
        x = self.next_value
        self.next_value = self._next()
        return x

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_value is not None


if __name__ == '__main__':
    def flattern(li):
        r = []
        it = NestedIterator2(li)
        while it.hasNext():
            r.append(it.next())
        return r

    assert flattern(NestedInteger.make_list([[1,1],2,[1,1]])) == [1, 1, 2, 1, 1]
    assert flattern(NestedInteger.make_list([[1,[4,[6]]]])) == [1, 4, 6]
