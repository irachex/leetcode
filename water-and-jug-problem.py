'''
https://leetcode.com/problems/water-and-jug-problem/

You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

Example 1: (From the famous "Die Hard" example)
Input: x = 3, y = 5, z = 4
Output: True

Example 2:
Input: x = 2, y = 6, z = 5
Output: False
'''


class Solution(object):

    def canMeasureWater(self, x, y, z):  # GCD
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(a, b):
            while b != 0:
                tmp = b
                b = a % b
                a = tmp
            return a

        if x + y < z:
            return False
        if x == z or y == z or x + y == z:
            return True
        return z % gcd(x, y) == 0

    def canMeasureWater_BFS(self, x, y, z):  # BFS, TLE
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        import collections
        visited = collections.defaultdict(dict)
        q = collections.deque([(0, 0)])
        while q:
            a, b = q.popleft()
            states = [
                (x, b),  # fill x
                (a, y),  # fill y
                (0, b),  # empty x
                (a, 0),  # empty y
                (a + min(x - a, b), b - min(x - a, b)),  # x -> y
                (a - min(y - b, a), b + min(y - b, a)),  # y -> x
            ]
            for u, v in states:
                if u < 0 or v < 0:
                    continue
                if u == z or v == z or u + v == z:
                    return True
                if not visited[u].get(v):
                    q.append((u, v))
                    visited[u][v] = True
        return z == 0


if __name__ == '__main__':
    f = Solution().canMeasureWater
    assert f(3, 5, 4)
    assert not f(2, 6, 5)
    assert not f(0, 0, 1)
    assert f(22003, 31237, 1)
    assert f(104597, 104623, 123)
