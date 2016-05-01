'''
https://leetcode.com/problems/nim-game/

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
'''

class Solution(object):

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

    def canWinNim_DP(self, n):  # MLE
        """
        :type n: int
        :rtype: bool
        """
        d = [False for i in range(n + 1)]
        d[0] = False
        for i in range(1, n + 1):
            for j in range(1, 4):
                if i - j >= 0:
                    d[i] = d[i] or not d[i - j]
        print d
        return d[n]


if __name__ == '__main__':
    f = Solution().canWinNim
    assert f(0) is False
    assert f(1) and f(2) and f(3)
    assert f(4) is False
