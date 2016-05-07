'''
https://leetcode.com/problems/word-ladder/

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        def is_connected(x, y):
            cnt = 0
            for i, c in enumerate(x):
                if y[i] != c:
                    cnt += 1
            return cnt == 1

        if is_connected(beginWord, endWord):
            return 2

        n = len(wordList) + 2
        edges = [[] for i in xrange(n)]
        table = None
        s, e = 0, 1  # beginWord is 0, endWord is 1
        for i, w in enumerate(wordList):
            x = i + 2
            if table is None:
                table = [{} for i in xrange(len(w))]
            if is_connected(beginWord, w):
                edges[s].append(x)
            if is_connected(w, endWord):
                edges[x].append(e)

            for j in xrange(len(w)):
                w2 = w[:j] + w[j + 1:]
                connected = table[j].get(w2)
                if connected is None:
                    table[j][w2] = connected = []
                else:
                    for y in connected:
                        edges[x].append(y)
                        edges[y].append(x)
                connected.append(x)

        d = [n + 1 for i in xrange(n)]
        d[s] = 1
        q = [0 for i in xrange(n)]
        b = [False for i in xrange(n)]
        head, tail, qsize = 0, 0, 1
        q[head] = s
        b[s] = True
        while qsize > 0:
            i = q[head]
            for j in edges[i]:
                if d[j] > d[i] + 1:
                    d[j] = d[i] + 1
                    if j == e:
                        return d[j]
                    if not b[j]:
                        b[j] = True
                        qsize += 1
                        tail += 1
                        if tail == n:
                            tail = 0
                        q[tail] = j
            b[i] = False
            qsize -= 1
            head += 1
            if head == n:
                head = 0

        return d[e] if d[e] <= n else 0


if __name__ == '__main__':
    f = Solution().ladderLength
    assert f("hit", "cog", {"hot","dot","dog","lot","log"}) == 5
    assert f("a", "c", ["a","b","c"]) == 2
