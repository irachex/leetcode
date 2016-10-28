'''
https://leetcode.com/problems/ransom-note/

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for c in magazine:
            d[c] = d.get(c, 0) + 1
        for c in ransomNote:
            d[c] = d.get(c, 0) - 1
            if d[c] < 0:
                return False
        return True


if __name__ == '__main__':
    f = Solution().canConstruct
    assert not f("a", "b")
    assert not f("aa", "ab")
    assert f("aa", "aab")
