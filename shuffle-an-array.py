'''
https://leetcode.com/problems/shuffle-an-array/

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
'''

import random


class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):  # Fisher Yates shuffle
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        a = self.nums[:]
        n = len(a)
        for i in xrange(n - 1):
            x = random.randint(0, n - i - 1)
            tmp = a[x]
            a[x] = a[n - i - 1]
            a[n - i - 1] = tmp
        return a


if __name__ == '__main__':
    f = Solution([1, 2, 3])
    print f.reset()
    print f.shuffle()
    print f.shuffle()
    print f.shuffle()
    print f.reset()
    print f.shuffle()
