'''
https://leetcode.com/problems/clone-graph/

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
'''

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """

        def dfs(p):
            if not p:
                return p
            node = UndirectedGraphNode(p.label)
            d[node.label] = node
            for nb in p.neighbors:
                c = d.get(nb.label)
                if c is None:
                    c = dfs(nb)
                node.neighbors.append(c)
            return node

        d = {}
        return dfs(node)
