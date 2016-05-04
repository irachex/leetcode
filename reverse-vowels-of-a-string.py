'''
https://leetcode.com/problems/reverse-vowels-of-a-string/

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ('a', 'e', 'i', 'o', 'u')
        i = 0
        j = len(s) - 1
        a = list(s)
        while i < j:
            while a[i].lower() not in vowels and i < j:
                i += 1
            while a[j].lower() not in vowels and i < j:
                j -= 1
            if i < j:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
                i += 1
                j -= 1
        return ''.join(a)


if __name__ == '__main__':
    f = Solution().reverseVowels
    assert f('aA') == 'Aa'
