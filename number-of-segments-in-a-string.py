'''
https://leetcode.com/problems/number-of-segments-in-a-string/

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
'''


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        space = True
        cnt = 0
        for c in s:
            if c in (' ', '\t', '\n'):
                space = True
            else:
                if space:
                    cnt += 1
                space = False
        return cnt

    def countSegments_split(self, s):
        return len(s.split())


if __name__ == '__main__':
    f = Solution().countSegments_split
    assert f('Hello, my name is John') == 5
    assert f('    a   b  c\nd\t\ne f') == 6
