#!/usr/bin/env python
from typing import List

class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        left = [[0 for _ in range(n)] for _ in range(n)]
        up = [[0 for _ in range(n)] for _ in range(n)]

        # 构建left矩阵
        for i in range(n):
            s = 0
            for j in range(n):
                if matrix[i][j] == 0:
                    s += 1
                    left[i][j] = s
                else:
                    s = 0

        # 构建up矩阵
        for j in range(n):
            s = 0
            for i in range(n):
                if matrix[i][j] == 0:
                    s += 1
                    up[i][j] = s
                else:
                    s = 0

        # 开始扫描每个位置
        res = [-1, -1, float('-inf')]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != 0: continue   # 如果某位置不是0，那么直接放弃探索
                limit = min(left[i][j], up[i][j])    # 确定其可能的最大边长
                e = 1
                for k in range(limit-1, -1, -1):    # 逐渐缩小可能边长
                    if up[i][j-k] > k and left[i-k][j] > k:
                        e = k + 1
                        break    # 因为边长是从大到小探索的，所以一旦发现一个符合条件的边长后可以直接break，无需探索更小的可能性。

                if e > res[2]:    # 记录结果
                    res = [i-e+1, j-e+1, e]    # 注意要求输出的坐标是子矩阵左上角的坐标，因此还要转换一下

        return res if res[2] > float('-inf') else []