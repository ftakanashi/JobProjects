#!/usr/bin/env python
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 预处理，将原数据左端的负数片和右端的正数片都单独拿出来
        head, tail = [], []
        n = len(asteroids)
        i, j = 0, n - 1
        while i < n and asteroids[i] < 0:
            head.append(asteroids[i])
            i += 1
        while j >= 0 and asteroids[j] > 0:
            tail.append(asteroids[j])
            j -= 1
        tail.reverse()

        stack = []
        for pos in range(i, j + 1):    # 从左到右遍历中间部分
            ast = asteroids[pos]
            if ast > 0:
                stack.append(ast)
            else:
                # 撞毁一片小正数，注意别忘了0 < stack[-1]这个条件
                while stack and 0 < stack[-1] < -ast:
                    stack.pop()

                if not stack or stack[-1] < 0:    # 前两种情况全部都入栈
                    stack.append(ast)
                elif stack[-1] == -ast:    # 相等重量星球互相毁灭
                    stack.pop()

        return head + stack + tail    # 最后结果别忘了预处理的两个数组