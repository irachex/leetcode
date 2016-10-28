# coding: utf-8

'''
https://leetcode.com/problems/fizz-buzz/

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a = []
        for i in xrange(1, n + 1):
            if i % 15 == 0:
                a.append('FizzBuzz')
            elif i % 3 == 0:
                a.append('Fizz')
            elif i % 5 == 0:
                a.append('Buzz')
            else:
                a.append(str(i))
        return a


if __name__ == '__main__':
    print Solution().fizzBuzz(15)
