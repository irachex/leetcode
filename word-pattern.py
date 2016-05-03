'''
https://leetcode.com/problems/word-pattern/

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words) != len(pattern):
            return False
        d = [None for i in range(26)]
        f = {}
        for i, w in enumerate(words):
            k = ord(pattern[i]) - ord('a')
            if d[k] is None and f.get(w) is None:
                d[k] = w
                f[w] = k
            elif d[k] != w or f[w] != k:
                return False
        return True


if __name__ == '__main__':
    f = Solution().wordPattern
    assert f('ab', 'dog dog') is False
    assert f('abba', 'dog cat cat dog')
    assert f('abba', 'dog cat cat fish') is False
    assert f('aaaa', 'dog cat cat dog') is False
    assert f('abba', 'dog dog dog dog') is False
    assert f('aaaa', 'dog dog dog dog')
