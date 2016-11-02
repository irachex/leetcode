'''
https://leetcode.com/problems/decode-string/

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        def decode(start):
            r = ''
            i = start
            while i < n:
                c = s[i]
                if c.isdigit():
                    num = 0
                    while s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    assert s[i] == '['
                    w, end = decode(i + 1)
                    r += w * num
                    i = end
                elif c == ']':
                    return r, i
                else:
                    r += c
                i += 1
            return r, i

        r, _ = decode(0)
        return r


if __name__ == '__main__':
    f = Solution().decodeString
    assert f('') == ''
    assert f("3[a]2[bc]") == "aaabcbc"
    assert f("3[a2[c]]") == "accaccacc"
    assert f("2[abc]3[cd]ef") == "abcabccdcdcdef"
