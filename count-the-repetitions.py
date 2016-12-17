# coding: utf-8

'''
https://leetcode.com/problems/count-the-repetitions/

Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".
On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, “abc” can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.
You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:
Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
'''


class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        repeat_count = [0]  # repeat_count[i] is the num of s2 after i(th) s1
        repeat_idx = [0]  # repeat_idx[i] is the idx of s2 at after i(th) s1
        idxs = {}  # idxs[idx] is the first i such that repeat_idx[i] == idxs[idx]
        len1, len2 = len(s1), len(s2)
        cycle_start = cycle_end = None
        cnt = p = 0
        for i in xrange(1, n1 + 1):
            for j in xrange(len1):
                if s1[j] == s2[p]:
                    p += 1
                    if p == len2:
                        p = 0
                        cnt += 1
            repeat_count.append(cnt)
            repeat_idx.append(p)
            if p in idxs:  # found a cycle
                cycle_start = idxs[p]
                cycle_end = i
                break
            else:
                idxs[p] = i

        if cycle_start is None:
            return cnt / n2
        cycle = cycle_end - cycle_start
        n_cycle = (n1 - cycle_start) / cycle
        n_repeat = n_cycle * (repeat_count[cycle_end] - repeat_count[cycle_start])
        n_remain = repeat_count[cycle_start + (n1 - cycle_start) % cycle]
        total = n_repeat + n_remain
        return total / n2


if __name__ == '__main__':
    f = Solution().getMaxRepetitions
    assert f("nlhqgllunmelayl", 2, "lnl", 1) == 3
    assert f('acb', 4, 'ab', 2) == 2
