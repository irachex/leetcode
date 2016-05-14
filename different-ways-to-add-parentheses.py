'''
https://leetcode.com/problems/different-ways-to-add-parentheses/

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
'''


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if not input:
            return []

        nums = []
        ops = []

        i = 0
        if not input[0].isdigit():
            nums.append(0)
            ops.append(input[0])
            i += 1
        x = 0
        while i < len(input):
            c = input[i]
            if c.isdigit():
                x = x * 10 + ord(c) - ord('0')
            else:
                nums.append(x)
                ops.append(c)
                x = 0
            i += 1
        nums.append(x)

        def calc(op, x, y):
            if op == '+':
                return x + y
            if op == '-':
                return x - y
            if op == '*':
                return x * y

        n = len(nums)
        d = [[[] for j in xrange(n)] for i in xrange(n)]
        for i in xrange(n):
            d[i][i].append(nums[i])
        for L in xrange(2, n + 1):
            for i in xrange(n - L + 1):
                j = i + L - 1
                for k in xrange(i, j):
                    for x in d[i][k]:
                        for y in d[k + 1][j]:
                            d[i][j].append(calc(ops[k], x, y))
        return d[0][n - 1]


if __name__ == '__main__':
    f = Solution().diffWaysToCompute
    print f("2-1-1")
    print f("2*3-4*5")
