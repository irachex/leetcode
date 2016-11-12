'''
https://leetcode.com/problems/reconstruct-original-digits-from-english/

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"
Output: "012"

Example 2:
Input: "fviefuro"
Output: "45"
'''


class Solution(object):
    def originalDigits(self, s):  # Gaussian elimination
        """
        :type s: str
        :rtype: str
        """
        words = ['zero', 'one', 'two', 'three', 'four',
                 'five', 'six', 'seven', 'eight', 'nine']
        n, m = 26, len(words)
        a = [[0.0 for j in xrange(m + 1)] for i in xrange(n)]
        for i, w in enumerate(words):
            for c in w:
                a[ord(c) - 97][i] += 1
        for c in s:
            a[ord(c) - 97][m] -= 1

        def find_row_by_max_abs(x, y):
            max_i = max_v = 0
            for i in xrange(x, n):
                if max_v < abs(a[i][y]):
                    max_v = a[i][y]
                    max_i = i
            return max_i if max_v > 1e-4 else None

        def swap_row(i, k):
            for j in xrange(m + 1):
                tmp = a[i][j]
                a[i][j] = a[k][j]
                a[k][j] = tmp

        i = j = 0
        while i < n and j < m:
            while j < m:
                k = find_row_by_max_abs(i, j)
                if k is not None:
                    break
                j += 1
            swap_row(i, k)
            for k in xrange(i + 1, n):
                if abs(a[k][j]) > 1e-4:
                    p = a[i][j] / a[k][j]
                    for t in xrange(j, m + 1):
                        a[k][t] = p * a[k][t] - a[i][t]
            i += 1
            j += 1
        f = [0 for i in xrange(m)]
        j = m - 1
        for i in reversed(xrange(m)):
            if abs(a[i][i]) < 1e-4:
                continue
            f[i] = -a[i][m]
            for t in xrange(i + 1, m):
                f[i] -= a[i][t] * f[t]
            f[i] /= a[i][i]

        return ''.join(chr(i + 48) * int(f[i] + 1e-4) for i in xrange(m))

    def originalDigits_bfs(self, s):  # TLE
        """
        :type s: str
        :rtype: str
        """
        words = ['zero', 'one', 'two', 'three', 'four',
                 'five', 'six', 'seven', 'eight', 'nine']
        a = [None for i in xrange(10)]
        for i, w in enumerate(words):
            a[i] = {}
            for c in w:
                a[i][c] = a[i].get(c, 0) + 1
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        q = [(d, '')]
        head = tail = 0
        while head <= tail:
            d, n = q[head]
            last = 0 if not n else int(n[-1])
            for i in xrange(last, 10):
                x = {c: v - a[i].get(c, 0) for c, v in d.iteritems()}
                if all(v >= 0 for v in x.itervalues()):
                    nn = n + str(i)
                    tail += 1
                    q.append((x, nn))
                    if all(v == 0 for v in x.itervalues()):
                        return nn
            head += 1


if __name__ == '__main__':
    f = Solution().originalDigits
    assert f('owoztneoer') == '012'
    assert f("zeroonetwothreefourfivesixseveneightnine") == '0123456789'
    assert f('fviefuro') == '45'
