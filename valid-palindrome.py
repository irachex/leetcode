#coding: utf-8

'''
http://oj.leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.\n\nFor example,"A man, a plan, a canal: Panama" is a palindrome."race a car" is not a palindrome.\n\nNote:
Have you consider that the string might be empty? This is a good question to ask during an interview.\nFor the purpose of this problem, we define empty string as valid palindrome.
'''

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
        a = ''.join(c.lower() for c in s if c.isalpha() or c.isdigit())
        return a == a[::-1]
