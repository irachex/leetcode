#coding: utf-8

'''
http://oj.leetcode.com/problems/scramble-string/

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of s1 = "great":
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.
For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".
Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        n = len(s1)
        if n == 1:
            return False
        c1 = list(sorted(s1))
        c2 = list(sorted(s2))
        if c1 != c2:
            return False
        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[:i]) and
                self.isScramble(s1[i:], s2[i:]) or
                self.isScramble(s1[:i], s2[n - i:]) and
                    self.isScramble(s1[i:], s2[:n - i])):
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.isScramble('great', 'rgtae')
    assert s.isScramble("abb", "bab")
