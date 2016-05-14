'''
https://leetcode.com/problems/repeated-dna-sequences/

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        L = 10
        d = {}
        for i, c in enumerate(s):
            if i >= L - 1:
                t = s[i - L + 1:i + 1]
                d[t] = d.get(t, 0) + 1
        return [k for k, cnt in d.iteritems() if cnt > 1]


if __name__ == '__main__':
    f = Solution().findRepeatedDnaSequences
    print f("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
