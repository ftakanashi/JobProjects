#!/usr/bin/env python
from typing import List

class Solution1:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                base = height[stack.pop()]
                if not stack: break
                l_height, r_height = height[stack[-1]], height[i]
                res += (min(l_height, r_height) - base) * (i - stack[-1] - 1)
            stack.append(i)
        return res

class Solution2:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0: return 0
        left_max, right_max = [0 for _ in range(n)], [0 for _ in range(n)]
        left_max[0], right_max[n-1] = height[0], height[n-1]

        # 第一次正向遍历，寻找每个位置其左边最高的值
        max_v = 0
        for i in range(n):
            if height[i] > max_v: max_v = height[i]
            left_max[i] = max_v

        # 第二次逆向遍历，寻找每个位置其右边最高的值
        max_v = 0
        for i in range(n-1, -1, -1):
            if height[i] > max_v: max_v = height[i]
            right_max[i] = max_v

        res = [min(left_max[i], right_max[i]) - height[i] for i in range(n)]
        return sum(res)