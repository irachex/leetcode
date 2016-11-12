'''
https://leetcode.com/problems/course-schedule-ii/

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
'''

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        d = [0 for i in xrange(numCourses)]
        e = [[] for i in xrange(numCourses)]
        for i, j in prerequisites:
            d[i] += 1
            e[j].append(i)
        q = []
        head = tail = 0
        for i in xrange(numCourses):
            if d[i] == 0:
                tail += 1
                q.append(i)
        while head < tail:
            i = q[head]
            for j in e[i]:
                d[j] -= 1
                if d[j] == 0:
                    tail += 1
                    q.append(j)
            head += 1
        return q if len(q) == numCourses else []


if __name__ == '__main__':
    f = Solution().findOrder
    print f(2, [[1,0]])
    print f(4, [[1,0],[2,0],[3,1],[3,2]])
    print f(3, [[0, 1], [1, 2], [2, 0]])
