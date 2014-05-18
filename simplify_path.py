#coding: utf-8

'''
http://oj.leetcode.com/problems/simplify-path/

Given an absolute path for a file (Unix-style), simplify it.
For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        paths = path.split('/')
        for p in paths:
            if p == '.' or not p:
                continue
            elif p == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        result = '/' + '/'.join(stack)
        return result


if __name__ == "__main__":
    s = Solution()
    testcases = [
        ('/home/', '/home'),
        ('/a/./b/../../c/', '/c'),
        ('/../', '/'),
        ('/home//foo/', '/home/foo'),
    ]
    for path, result in testcases:
        assert s.simplifyPath(path) == result
