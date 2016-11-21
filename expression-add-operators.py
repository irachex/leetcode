'''
https://leetcode.com/problems/expression-add-operators/

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
'''

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        num = [int(c) for c in num]
        n = len(num)
        result = []

        def dfs(i, expression, value, last):
            if i == n:
                if value == target:
                    result.append(expression)
                return

            x = 0
            xs = ''
            for j in xrange(i, n):
                x = x * 10 + num[j]
                xs += chr(num[j] + 48)
                if num[i] == 0 and j > i:
                    break
                if i == 0:
                    dfs(j + 1, xs, x, x)
                    continue
                dfs(j + 1, expression + '+' + xs, value + x, x)
                dfs(j + 1, expression + '-' + xs, value - x, -x)
                dfs(j + 1, expression + '*' + xs, value - last + last * x, last * x)

        dfs(0, '', 0, 0)
        return result


if __name__ == '__main__':
    f = Solution().addOperators
    print f('123456789', 45)
    assert f("123", 6) == ["1+2+3", "1*2*3"]
    assert f("232", 8) == ["2+3*2", "2*3+2"]
    assert f("105", 5) == ["1*0+5", "10-5"]
    assert f("00", 0) == ["0+0", "0-0", "0*0"]
    assert f("3456237490", 9191) == []
