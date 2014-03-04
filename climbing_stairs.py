"""
http://oj.leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n < 2:
            return 1
        a = b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c


if __name__ == "__main__":
    s = Solution()
    assert s.climbStairs(1) == 1
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(4) == 5
