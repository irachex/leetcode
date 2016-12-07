'''
https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 1 is the only number in the set, getRandom always return 1.
randomSet.getRandom();
'''

import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.id_mapping = {}
        self.data = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.id_mapping:
            return False
        self.data.append(val)
        self.id_mapping[val] = len(self.data) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.id_mapping:
            return False
        i = self.id_mapping.pop(val)
        if i != len(self.data) - 1:
            self.data[i] = self.data[-1]
            self.id_mapping[self.data[i]] = i
        self.data.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.data[random.randint(0, len(self.data) - 1)]


if __name__ == '__main__':
    s = RandomizedSet()
    print s.insert(0)
    print s.remove(0)
    print s.insert(-1)
    print s.remove(0)
    print s.getRandom()
    print s.getRandom()
