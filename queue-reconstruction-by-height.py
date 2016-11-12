'''
https://leetcode.com/problems/queue-reconstruction-by-height/

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for h, k in sorted(people, key=lambda (h, k): (-h, k)):
            result.insert(k, [h, k])
        return result

    def reconstructQueue2(self, people):  # O(n^2) but get TLE
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(people)
        p = [[h, k] for h, k in people]
        result = []
        while len(result) < n:
            min_h = 2 << 31
            min_i = 0
            for i, (h, k) in enumerate(p):
                if min_h > h and k == 0:
                    min_h = h
                    min_i = i
            p[min_i][1] = -1
            result.append(people[min_i])
            for i, (h, k) in enumerate(p):
                if k > 0 and min_h >= h:
                    p[i][1] -= 1
        return result


if __name__ == '__main__':
    f = Solution().reconstructQueue
    assert f([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]) == [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
