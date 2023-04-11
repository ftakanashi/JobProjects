#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = d = 0
        move_mapping = {    # 朝向与位移对应到坐标变化
            0: (0, 1),
            1: (1, 0),
            2: (0, -1),
            3: (-1, 0),
        }

        # 进行一轮操作，看最终位置判断答案
        for move in instructions:
            if move == "G":
                moves = move_mapping[d]
                x += moves[0]
                y += moves[1]
            elif move == "L":
                d -= 1
                if d < 0: d = 3
            else:
                d = (d + 1) % 4

        return (x, y) == (0, 0) or d != 0