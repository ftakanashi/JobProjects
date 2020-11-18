#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tmp = [gas[i] - cost[i] for i in range(len(gas))]
        start = 0
        rest = total = 0
        # rest 用于维护当前遍历轮的起点到当前节点的汽油净剩余量
        # total 用于维护从0号开始行进到当前节点的汽油净剩余量
        # rest < 0，表示当前遍历轮的起点走不到当前节点的下一节点 因此可以直接把开始节点指定为当前节点的下一节点，再检查
        for i in range(len(tmp)):
            rest += tmp[i]
            total += tmp[i]

            if rest < 0:
                start = i + 1
                rest = 0

        return start if total >= 0 else -1