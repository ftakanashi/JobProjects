#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 初始化
        rows = [0 for _ in range(9)]
        cols = [0 for _ in range(9)]
        boxes = [0 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                box_i = (i // 3) * 3 + (j // 3)
                n = board[i][j]
                if n == '.':
                    continue
                else:
                    n = int(n)

                    if (rows[i] >> (n-1) & 1 == 1 or cols[j] >> (n-1) & 1 == 1 or
                            boxes[box_i] >> (n-1) & 1 == 1):
                        # 如果数字n已经存在于当前位置所在行，或者所在列，或者所在小宫中
                        return False

                    # 维护数字n进行、列、小宫二进制数的相应位置，表示这个数已经存在于数独的相应位置了
                    # 之后如果同行同列同小宫有相同元素，就不行啦
                    rows[i] = rows[i] | 1 << (n-1)
                    cols[j] = cols[j] | 1 << (n-1)
                    boxes[box_i] = boxes[box_i] | 1 << (n-1)
        return True