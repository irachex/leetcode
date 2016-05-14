'''
https://leetcode.com/problems/course-schedule/

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
'''


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        d = [0 for i in xrange(numCourses)]
        e = [[] for i in xrange(numCourses)]
        for i, j in prerequisites:
            d[j] += 1
            e[i].append(j)
        q = []
        qsize = 0
        for i in xrange(numCourses):
            if d[i] == 0:
                qsize += 1
                q.append(i)
        top = 0
        while top < qsize:
            i = q[top]
            for j in e[i]:
                d[j] -= 1
                if d[j] == 0:
                    qsize += 1
                    q.append(j)
            top += 1
        return len(q) == numCourses


if __name__ == '__main__':
    f = Solution().canFinish
    assert f(2, [[1, 0]])
    assert f(4, [[0, 1], [1, 2], [3, 2]])
    assert not f(2, [[1, 0], [0, 1]])
    assert not f(3, [[1, 0], [0, 1]])
