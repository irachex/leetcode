'''
https://leetcode.com/problems/maximum-product-of-word-lengths/

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
'''

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        b = [0 for i in xrange(n)]
        for i, word in enumerate(words):
            for c in word:
                b[i] |= 1 << (ord(c) - ord('a'))

        ans = 0
        for i in xrange(n):
            for j in xrange(i + 1, n):
                if b[i] & b[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans


if __name__ == '__main__':
    f = Solution().maxProduct
    assert f(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
    assert f(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4
    assert f(["a", "aa", "aaa", "aaaa"]) == 0
