#coding: utf-8

'''
http://oj.leetcode.com/problems/count-and-say/

The count-and-say sequence is the sequence of integers beginning as follows:1, 11, 21, 1211, 111221, ...
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.
'''

class Solution:
    # @return a string
    def countAndSay(self, n):

        def say(num):
            cnt = 0
            current = ''
            s = ''
            for i, c in enumerate(str(num) + '$'):
                if i > 0 and c == current:
                    cnt += 1
                else:
                    if current:
                        s += str(cnt) + current
                    current = c
                    cnt = 1
            return s

        num = 1
        s = str(num)
        for i in range(1, n):
            s = say(num)
            num = int(s)
        return s


if __name__ == "__main__":
    print Solution().countAndSay(4)
