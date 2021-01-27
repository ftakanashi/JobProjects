#!/usr/bin/env python
from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(T) - 1, -1, -1):
            # 注意stack内部保存的是下标而不是温度值
            while len(stack) > 0 and T[stack[-1]] <= T[i]:
                stack.pop()
            if len(stack) == 0:
                res.append(len(T))    # 栈为空时加入哨兵节点。
            else:
                res.append(stack[-1])
            stack.append(i)

        res.reverse()    # 由于是从右往左扫描，记得reverse
        return [res[i] - i if res[i] != len(T) else 0 for i in range(len(res))]