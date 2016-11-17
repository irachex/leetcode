'''
https://leetcode.com/problems/remove-duplicate-letters/

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
'''


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        stack = []
        in_stack = {}
        for c in s:
            if not in_stack.get(c):
                while stack and c < stack[-1] and d[stack[-1]] > 0:
                    top = stack.pop()
                    in_stack.pop(top)
                stack.append(c)
                in_stack[c] = True
            d[c] -= 1
        return ''.join(stack)


if __name__ == '__main__':
    f = Solution().removeDuplicateLetters
    assert f("abacb") == 'abc'
    assert f("bbcaac") == 'bac'
    assert f("baab") == 'ab'
    assert f('baa') == 'ba'
    assert f("bcabc") == "abc"
    assert f("cbacdcbc") == "acdb"
