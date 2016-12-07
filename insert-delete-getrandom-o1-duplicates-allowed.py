'''
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
'''

import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.id_mapping = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ret = val not in self.id_mapping
        self.data.append(val)
        if val in self.id_mapping:
            self.id_mapping[val].add(len(self.data) - 1)
        else:
            self.id_mapping[val] = {len(self.data) - 1}
        return ret

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.id_mapping:
            return False
        ids = self.id_mapping[val]
        i = ids.pop()
        if not self.id_mapping[val]:
            self.id_mapping.pop(val)
        if i != len(self.data) - 1:
            self.data[i] = self.data[-1]
            self.id_mapping[self.data[i]].remove(len(self.data) - 1)
            self.id_mapping[self.data[i]].add(i)
        self.data.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.data[random.randint(0, len(self.data) - 1)]


if __name__ == '__main__':
    s = RandomizedCollection()
    print [s.insert(10), s.insert(10), s.insert(20), s.insert(20), s.insert(30), s.insert(30),
           s.remove(10), s.remove(10), s.remove(30), s.remove(30), s.getRandom(), s.getRandom()]
    s = RandomizedCollection()
    print [s.insert(1), s.insert(1), s.remove(1), s.getRandom()]
