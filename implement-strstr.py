'''
https://leetcode.com/problems/implement-strstr/

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''


def gen_next(p):
    n = len(p)
    # next[i] = j if exist j such that p[0..j] == p[i-j..i] else -1
    next = [0 for i in xrange(n)]
    next[0] = -1
    j = -1
    for i in xrange(1, n):
        while j >= 0 and p[i] != p[j + 1]:
            j = next[j]
        if p[i] == p[j + 1]:
            j += 1
        next[i] = j
    return next


def kmp(s, p):
    if not p:
        yield 0
    next = gen_next(p)
    n = len(s)
    m = len(p)
    j = -1
    for i in xrange(n):
        while j >= 0 and s[i] != p[j + 1]:
            j = next[j]
        if s[i] == p[j + 1]:
            j += 1
        if j == m - 1:
            yield i - m + 1
            j = p[j]
    yield -1


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return next(kmp(haystack, needle))

    def strStr_index(self, haystack, needle):
        try:
            return haystack.index(needle)
        except ValueError:
            return -1


if __name__ == '__main__':
    f = Solution().strStr
    assert f('abababaababacb', 'ababacb') == 7
    assert f('ababcbcasf', 'cbca') == 4
    assert f('ababcbcasf', 'cbcaa') == -1
    assert f('ababcbcasf', '') == -1
