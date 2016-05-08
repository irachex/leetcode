'''
https://leetcode.com/problems/word-ladder-ii/

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
'''

class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        def is_connected(x, y):
            cnt = 0
            for i, c in enumerate(x):
                if y[i] != c:
                    cnt += 1
            return cnt == 1

        if is_connected(beginWord, endWord):
            return [[beginWord, endWord]]

        n = len(wordlist) + 2
        words = [0 for i in xrange(n)]
        words[0] = beginWord
        words[1] = endWord
        edges = [[] for i in xrange(n)]
        table = None
        s, e = 0, 1  # beginWord is 0, endWord is 1
        for i, w in enumerate(wordlist):
            x = i + 2
            words[x] = w
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
        p = [[] for i in xrange(n)]
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
                    p[j].append(i)
                    if not b[j]:
                        b[j] = True
                        qsize += 1
                        tail += 1
                        if tail == n:
                            tail = 0
                        q[tail] = j
                elif d[j] == d[i] + 1:
                    p[j].append(i)
            b[i] = False
            qsize -= 1
            head += 1
            if head == n:
                head = 0

        if d[e] > n:
            return []

        result = []
        a = [0 for j in xrange(d[e])]

        def dfs(dep, i):
            a[dep] = i
            if i == s:
                result.append([words[x] for x in reversed(a)])
                return

            for j in p[i]:
                dfs(dep + 1, j)

        dfs(0, e)
        return result


if __name__ == '__main__':
    f = Solution().findLadders
    print f("hit", "cog", {"hot","dot","dog","lot","log"})
    print f("a", "c", ["a","b","c"])
