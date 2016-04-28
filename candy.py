# coding: utf-8

'''
https://leetcode.com/problems/candy/

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''


class Solution(object):

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n <= 1:
            return n
        q = []
        d = [0 for i in range(n)]
        for i, x in enumerate(ratings):
            if (i == 0 and x <= ratings[i + 1] or
                    i == len(ratings) - 1 and x <= ratings[i - 1] or
                    x <= ratings[i - 1] and x <= ratings[i + 1]):
                q.append(i)
                d[i] = 1
        top = 0
        while top < len(q):
            i = q[top]
            d[i] = max(d[i],
                       d[i - 1] + 1 if i > 0 and ratings[i] > ratings[i - 1] else 0,
                       d[i + 1] + 1 if i < n - 1 and ratings[i] > ratings[i + 1] else 0)
            if i > 0 and ratings[i - 1] > ratings[i]:
                if d[i - 1] == 0:
                    q.append(i - 1)
                d[i - 1] = max(d[i - 1], d[i] + 1)
            if i < n - 1 and ratings[i + 1] > ratings[i]:
                if d[i + 1] == 0:
                    q.append(i + 1)
                d[i + 1] = max(d[i + 1], d[i] + 1)
            top += 1
        return sum(d)


if __name__ == '__main__':
    s = Solution()
    assert s.candy([3, 2, 1, 1, 2, 3, 2, 3]) == sum([3, 2, 1, 1, 2, 3, 1, 2])
