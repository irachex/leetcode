'''
https://leetcode.com/problems/evaluate-division/

Equations are given in the format A / B = k, where A and B are variables represefnted as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        f = {}
        w = {}

        def father(x):
            if x not in f:
                f[x] = x
                w[x] = 1
                return x
            if f[x] == x:
                return x
            r = father(f[x])
            w[x] *= w[f[x]]
            f[x] = r
            return r

        for i, (u, v) in enumerate(equations):
            fu = father(u)
            fv = father(v)
            if fu != fv:
                f[fu] = fv
                # (w[u] * fu) / (w[v] * fv) = values[i]
                w[fu] = values[i] * w[v] / w[u]

        result = []
        for u, v in queries:
            if u not in f or v not in f:  # x/x -1.0
                result.append(-1.0)
                continue
            fu = father(u)
            fv = father(v)
            if fu != fv:
                result.append(-1.0)
            else:
                result.append(w[u] / w[v])
        return result


if __name__ == '__main__':
    f = Solution().calcEquation
    print f([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])
