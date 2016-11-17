'''
https://leetcode.com/problems/palindrome-pairs/

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''


class TrieNode(dict):
    def __init__(self):
        self['value'] = None
        self['ids'] = []

    @property
    def value(self):
        return self['value']

    @value.setter
    def value(self, value):
        self['value'] = value

    @property
    def ids(self):
        return self['ids']


def is_palindrome(s, start, end):
    for i in xrange(start, end):
        if s[i] != s[start + end - i]:
            return False
    return True


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        root = TrieNode()
        for i, s in enumerate(words):
            n = len(s)
            node = root
            for j, c in enumerate(reversed(s)):
                if is_palindrome(s, 0, n - j - 1):
                    node.ids.append(i)
                next = node.get(c)
                if next is None:
                    node[c] = next = TrieNode()
                node = next
            node.value = i

        result = []
        for i, s in enumerate(words):
            node = root
            n = len(s)
            for j, c in enumerate(s):
                if node.value is not None and node.value != i and is_palindrome(s, j, n - 1): # is_palindrome[i][j][n - 1]:
                    result.append([i, node.value])
                node = node.get(c)
                if not node:
                    break
            if node:
                if node.value is not None and node.value != i:
                    result.append([i, node.value])
                result.extend([i, j] for j in node.ids)

        return result


if __name__ == '__main__':
    f = Solution().palindromePairs
    print f(["bat", "tab", "cat"])  # [[0, 1], [1, 0]]
    print f(["abcd", "dcba", "lls", "s", "sssll"])  # [[0, 1], [1, 0], [3, 2], [2, 4]]
    print f(["", "abcba", 'ab'])  # [[0, 1], [1, 0]]
