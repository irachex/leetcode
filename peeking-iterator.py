'''
https://leetcode.com/problems/peeking-iterator/

Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.
'''

# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.i = 0
        self.nums = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.i < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        r = self.nums[self.i]
        self.i += 1
        return r

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.next_cnt = 0
        self._preload_next()

    def _preload_next(self):
        if self.iter.hasNext():
            self.next_val = self.iter.next()
            self.next_cnt = 1
        else:
            self.next_cnt -= 1

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_val

    def next(self):
        """
        :rtype: int
        """
        r = self.next_val
        self._preload_next()
        return r

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_cnt > 0


if __name__ == '__main__':
    def test_iter(nums):
        iter = PeekingIterator(Iterator(nums))
        while iter.hasNext():
            val = iter.peek()   # Get the next element but not advance the iterator.
            print val
            print iter.next()         # Should return the same value as [val].

    test_iter([1, 2, 3, 4, 5])
    print '-' * 40
    test_iter([])
    print '-' * 40
    test_iter([1])
