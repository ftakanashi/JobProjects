#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import deque, defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        # 判断炸弹b1爆炸后能否触发炸弹b2
        def can_trigger(b1, b2):
            x1, y1, r1 = b1
            x2, y2, r2 = b2
            return r1 ** 2 >= ((x1 - x2) ** 2 + (y1 - y2) ** 2)

        # 构建有向图
        graph = defaultdict(set)
        for i in range(n):
            for j in range(i + 1, n):
                if can_trigger(bombs[i], bombs[j]): graph[i].add(j)
                if can_trigger(bombs[j], bombs[i]): graph[j].add(i)

        ans = 0
        # 从每个炸弹作为起爆点，开始BFS
        for i in range(n):
            q = deque([i, ])
            seen = {i, }
            res = 1
            while q:
                b = q.popleft()
                for nxt in graph[b]:
                    if nxt in seen: continue
                    res += 1
                    q.append(nxt)
                    seen.add(nxt)
            ans = max(ans, res)    # res是每个起爆点对应的最大可引爆炸弹数量

        return ans