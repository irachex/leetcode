'''
https://leetcode.com/problems/lexicographical-numbers/

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
'''


class Solution(object):

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        x = 1
        for i in xrange(n):
            result.append(x)
            if x * 10 <= n:
                x *= 10
            else:
                x += 1
                while x % 10 == 0:
                    x /= 10
                if x > n:
                    x = x / 10 + 1
        return result

    def lexicalOrder_dfs(self, n):  # MLE
        """
        :type n: int
        :rtype: List[int]
        """
        total_digits = len(str(n))
        result = []

        def gen(n_digits, x):
            for i in xrange(0 if x else 1, 10):
                y = x * 10 + i
                if y <= n:
                    result.append(y)
                    if n_digits < total_digits:
                        gen(n_digits + 1, y)
                else:
                    break

        gen(0, 0)
        return result


if __name__ == '__main__':
    f = Solution().lexicalOrder
    assert f(0) == []
    assert f(13) == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
    print f(100)
    f(49999)
