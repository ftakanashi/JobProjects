#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # 构建棋盘，即 字母 -> 坐标 对应
        grid = {}
        for i in range(26):
            grid[chr(ord('a') + i)] = (i // 5, i % 5)

        last = 'a'    # 从a开始
        ans = ""
        for ch in target:
            # 模拟从 last 走到 ch 的过程
            if ch == last:    # 若两者相同，则直接加感叹号并返回，不用走格子
                ans += '!'
                continue

            # 如果终点是z且起点不是z，需要做特殊处理，暂时将终点设置为u，然后最后手动加上一个D
            z_flag = False
            if ch == 'z':
                ch = 'u'
                z_flag = True

            diff = (grid[ch][0] - grid[last][0], grid[ch][1] - grid[last][1])

            if diff[0] >= 0:
                ans += 'D' * diff[0]
            else:
                ans += 'U' * -diff[0]

            if diff[1] >= 0:
                ans += 'R' * diff[1]
            else:
                ans += 'L' * -diff[1]

            if z_flag:
                ans += 'D'
                ch = 'z'

            ans += '!'
            last = ch

        return ans