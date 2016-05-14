'''
https://leetcode.com/problems/gas-station/

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        start = n - 1
        end = 0
        s = gas[start] - cost[start]
        while start > end:
            if s >= 0:
                s += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                s += gas[start] - cost[start]
        return start if s >= 0 else -1

    def canCompleteCircuit_greedy(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        a = [0 for i in xrange(n)]
        for i in xrange(n):
            a[i] = gas[i] - cost[i]
        if n == 1:
            return 0 if a[0] >= 0 else -1

        def check(i):
            s = 0
            for j in xrange(n):
                if s + a[(i + j) % n] < 0:
                    return False
                s += a[(i + j) % n]
            return s >= 0

        for i in xrange(n):
            if a[i - 1] < 0 and a[i] > 0 and check(i):
                return i
        return -1


if __name__ == '__main__':
    f = Solution().canCompleteCircuit
