#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution2:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0:
            return False

        row = 0
        col = len(array[0]) - 1

        while row < len(array) and col >= 0:    # 注意只要行或者列超过界限，则表明可选区域已经为空，所以是and
            n = array[row][col]
            if n > target:
                col -= 1
            elif n < target:
                row += 1
            else:
                return True

        return False