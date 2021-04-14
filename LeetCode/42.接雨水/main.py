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
        left_max, right_max = [], []
        n = len(height)

        # 第一次正向遍历，寻找每个位置其左边最高的值
        max_v = 0
        for i in range(n):
            if height[i] > max_v:
                max_v = height[i]
            left_max.append(max_v)

        # 第二次逆向遍历，寻找每个位置其右边最高的值
        max_v = 0
        for i in range(n-1, -1, -1):
            if height[i] > max_v:
                max_v = height[i]
            right_max.append(max_v)
        right_max.reverse()    # 最后别忘了reverse

        res = 0
        for i in range(n):
            res += max(min(left_max[i], right_max[i]) - height[i], 0)

        return res