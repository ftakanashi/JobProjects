#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 一些前处理
        X, Y = len(board), len(board[0])
        checked = [[0 for _ in range(Y)] for _ in range(X)]    # 检查字符是否被使用矩阵。0代表未使用；1代表已经使用
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, n):
            '''
            :param x: 当前位置x坐标
            :param y: 当前位置y坐标
            :param n: 当前需要匹配的是word的第n个字符
            '''
            target_ch = word[n]
            if board[x][y] != target_ch or checked[x][y] == 1:
                return False

            # 走到这里时说明当前位置匹配了要匹配的字符并且它也没被使用
            # 如果此时n还是word.length - 1即最后一个字符了，那么就可以直接返回True了。
            if n == len(word) - 1:
                return True

            # 标记被使用
            checked[x][y] = 1
            for a, b in direc:
                if 0 <= x + a < X and 0 <= y + b < Y:
                    if dfs(x + a, y + b, n + 1):    # 只有找到一条可行的路才行
                        return True

            # 走到这说明当前位置伸出的所有触手都是死路，只能作罢。别忘了重置checked的数据
            checked[x][y] = 0
            return False

        for x in range(X):
            for y in range(Y):
                if dfs(x, y, 0): return True

        return False