'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m = len(p)
        cp = [0 for i in xrange(26)]
        for c in p:
            cp[ord(c) - 97] += 1
        cs = [0 for i in xrange(26)]
        result = []
        for i, c in enumerate(s):
            cs[ord(c) - 97] += 1
            if i >= m - 1:
                if all(cp[j] == cs[j] for j in xrange(26)):
                    result.append(i - m + 1)
                cs[ord(s[i - m + 1]) - 97] -= 1
        return result


if __name__ == '__main__':
    f = Solution().findAnagrams
    assert f('cbaebabacd', 'abc') == [0, 6]
    assert f('abab', 'ab') == [0, 1, 2]
