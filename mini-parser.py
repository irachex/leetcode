'''
https://leetcode.com/problems/mini-parser/

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
'''


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.value = value if value is not None else []

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return isinstance(self.value, int)

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.value.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.value = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.value if self.isInteger() else None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.value if not self.isInteger() else None

    def __repr__(self):
        return repr(self.value)


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        s += '$'
        n = len(s)

        def dfs(i, container=None):
            sign = 1
            x = 0
            r = None
            is_integer = False
            while i < n:
                c = s[i]
                if c.isdigit() or c == '-':
                    is_integer = True
                    if c == '-':
                        sign = -1
                    else:
                        x = x * 10 + ord(c) - 48
                else:
                    if c == '[':
                        ret, end = dfs(i + 1, NestedInteger())
                        if container:
                            container.add(ret)
                        else:
                            r = ret
                        i = end
                    elif c == ']':
                        if is_integer:
                            container.add(NestedInteger(sign * x))
                        return container, i
                    elif c == ',':
                        if is_integer:
                            container.add(NestedInteger(sign * x))
                    elif c == '$':
                        if r is None:
                            r = NestedInteger(sign * x)
                    is_integer = False
                    x = 0
                    sign = 1
                i += 1
            return r, i

        return dfs(0)[0]


if __name__ == '__main__':
    f = Solution().deserialize
    print f('[-1,-2,[-3,[-4],-5]]')
    print f('-3')
    print f("[123,[456,[789]]]")
    print f('324')
