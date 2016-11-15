"""
http://oj.leetcode.com/problems/roman-to-integer/

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    # @return an integer
    def romanToInt(self, s):
        R = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        d = map(R.get, list(s))
        ans = d[-1]
        for i in range(len(d) - 2, -1, -1):
            if d[i] < d[i + 1]:
                ans -= d[i]
            else:
                ans += d[i]
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.romanToInt('XIX') == 19
    assert s.romanToInt('LXXIX') == 79
    assert s.romanToInt('DCCVII') == 707
    assert s.romanToInt('MDCCC') == 1800
