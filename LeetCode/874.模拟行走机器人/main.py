#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = x = y = d = 0
        dm = [0, 1, 2, 3]
        direcs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set(tuple(o) for o in obstacles)
        for cmd in commands:
            if cmd == -2:
                d = dm[d - 1]
            elif cmd == -1:
                d = dm[(d + 1) % 4]
            else:
                dx, dy = direcs[d]
                for _ in range(cmd):
                    nx, ny = x+dx, y+dy
                    if (nx, ny) in obstacles: break
                    x, y = nx, ny
            ans = max(ans, (x ** 2 + y ** 2))

        return ans