#coding: utf-8

'''
http://oj.leetcode.com/problems/edit-distance/

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:
a) Insert a character
b) Delete a character
c) Replace a character
'''

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)

        d = [[n + m for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    d[i][j] = min(d[i][j], d[i - 1][j - 1])
                d[i][j] = min(
                    d[i][j],
                    d[i - 1][j] + 1,  # delete
                    d[i][j - 1] + 1,  # insert
                    d[i - 1][j - 1] + 1,  # replace
                )
        return d[n][m]


if __name__ == "__main__":
    s = Solution()
    assert s.minDistance("sea", "eat") == 2
