#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        q = deque()
        q.append((0, 0, 0))   # 三个数字分别表示当前位置、上次是否向左跳（1是0否）、走过的总步数
        seen = {0, }
        upper = max(max(forbidden) + a, x) + b
        while q:
            pos, back, steps = q.popleft()
            if pos == x:
                return steps
            if back == 0:
                n = pos - b
                if n > 0 and n not in forbidden and n not in seen:
                    q.append((n, back + 1, steps + 1))
                    seen.add(n)
            n = pos + a
            if n <= upper and n not in forbidden and n not in seen:
                q.append((n, 0, steps + 1))
                seen.add(n)

        return -1