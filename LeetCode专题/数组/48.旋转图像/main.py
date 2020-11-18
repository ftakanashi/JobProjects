#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for layer in range(n // 2):    # n为偶数时共有 n // 2 层，n为奇数时虽然有n//2 + 1层，但是最后一层即中心只有一个元素，不用管
            for j in range(layer, n - layer - 1):
                # 遍历每层的上边作为每个小组rotate的入口。注意遍历从上边的第一个元素到倒数第二个，因为最后一个元素和第一个是同一小组

                # 以下是每个小组的rotate过程。其实因为固定是交换四次，所以也可以不用while而用for _ in range(4)
                tmp = matrix[layer][j]
                x, y = j, n - 1 - layer
                while (x, y) != (layer, j):
                    matrix[x][y], tmp = tmp, matrix[x][y]
                    x, y = y, n - 1 - x
                matrix[x][y] = tmp

class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):    # 注意转置操作中第二层循环的开始下标
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()