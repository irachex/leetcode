'''
https://leetcode.com/problems/compare-version-numbers/

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        if len(v2) < len(v1):
            v2.extend([0] * (len(v1) - len(v2)))
        elif len(v1) < len(v2):
            v1.extend([0] * (len(v2) - len(v1)))
        if v1 > v2:
            return 1
        elif v1 == v2:
            return 0
        else:
            return -1


if __name__ == '__main__':
    f = Solution().compareVersion
    assert f('0.1', '1.1') == -1
    assert f('0.12', '0.13') == -1
    assert f('1.2', '1.1') == 1
    assert f('2.3.4', '2.3.4') == 0
    assert f('1.0', '1') == 0
    assert f('2', '1.2') == 1
