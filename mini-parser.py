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
        n = len(s)

        def dfs(i):
            if s[i] == '[':
                r = NestedInteger()
                i += 1
                while i < n:
                    if s[i] == '[':
                        x, i = dfs(i)
                        r.add(x)
                    elif s[i] == ']':
                        return r, i + 1
                    elif s[i].isdigit() or s[i] == '-':
                        x, i = dfs(i)
                        r.add(x)
                    else:
                        i += 1
            else:
                x, sign = 0, 1
                while i < n and (s[i].isdigit() or s[i] == '-'):
                    if s[i] == '-':
                        sign = -1
                    else:
                        x = x * 10 + ord(s[i]) - 48
                    i += 1
                r = NestedInteger(sign * x)
            return r, i

        return dfs(0)[0]


if __name__ == '__main__':
    f = Solution().deserialize
    print f('[123,456,[788,799,833],[[]],10,[]]')
    print f('[-1,-2,[-3,[-4],-5]]')
    print f('-3')
    print f("[123,[456,[789]]]")
    print f('324')
