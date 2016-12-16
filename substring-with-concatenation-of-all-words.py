'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        m = len(words)
        L = len(words[0])
        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1
        result = []
        for i in xrange(len(s) - m * L + 1):
            c = {}
            count = 0
            for j in xrange(m):
                w = s[i + j * L:i + (j + 1) * L]
                if c.get(w, 0) < d.get(w, 0):
                    c[w] = c.get(w, 0) + 1
                    count += 1
                else:
                    break
            if count == m:
                result.append(i)
        return result


if __name__ == '__main__':
    f = Solution().findSubstring
    assert f('barfoothefoobarman', ['foo', 'bar']) == [0, 9]
