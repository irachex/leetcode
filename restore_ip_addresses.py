#coding: utf-8

'''
http://oj.leetcode.com/problems/restore-ip-addresses/

Given a string containing only digits, restore it by returning all possible valid IP address combinations.
For example:
Given "25525511135",
return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        n = len(s)
        result = []

        def dfs(i, part, a):
            if part > 4:
                return
            if i == n:
                if part == 4:
                    result.append(a)
                return

            for j in range(1, 4):
                if i + j <= n:
                    x = s[i:i + j]
                    x_int = int(x)
                    if x_int < 256 and len(str(x_int)) == j:
                        dfs(i + j, part + 1, a + '.' + x if part > 0 else x)

        dfs(0, 0, '')

        return result


if __name__ == "__main__":
    s = Solution()
    print s.restoreIpAddresses('25525511135')
    print s.restoreIpAddresses('0000')
    print s.restoreIpAddresses('010010')
