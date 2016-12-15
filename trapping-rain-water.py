'''
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = height
        n = len(a)
        i, j = 0, n - 1
        ans = max_left = max_right = 0
        while i <= j:
            if a[i] < a[j]:
                if a[i] > max_left:
                    max_left = a[i]
                else:
                    ans += max_left - a[i]
                i += 1
            else:
                if a[j] > max_right:
                    max_right = a[j]
                else:
                    ans += max_right - a[j]
                j -= 1
        return ans

    def trap_DP(self, a):
        n = len(a)
        left = [0 for i in xrange(n)]
        right = [0 for j in xrange(n)]
        for i in xrange(n):
            left[i] = max(left[i - 1], a[i]) if i > 0 else a[i]
            j = n - 1 - i
            right[j] = max(right[j + 1], a[j]) if j < n - 1 else a[j]
        ans = 0
        for i in xrange(n):
            ans += min(left[i], right[i]) - a[i]
        return ans

    def trap_stack(self, a):
        n = len(a)
        ans = 0
        stack = []
        for i in xrange(n + 1):
            h = a[i] if i < n else 0
            if not stack or h <= a[stack[-1]]:
                stack.append(i)
            else:
                while stack and h > a[stack[-1]]:
                    bottom = stack.pop()
                    ans += (min(a[i], a[stack[-1]]) - a[bottom]) * (i - stack[-1] - 1) if stack else 0
                stack.append(i)
        return ans


if __name__ == '__main__':
    f = Solution().trap_stack
    assert f([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
