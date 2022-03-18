#!/usr/bin/env python
from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        row_indices = []
        col_indices = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_indices.append(i)
                    col_indices.append(j)
        col_indices.sort()    # 由于本身是从上至下遍历的，所以行坐标序列天生有序，无序再sort一次

        ans = 0    # 最终求的总距离就是行方向距离和+列方向距离和，所以直接在两个序列上分别遍历即可，无序二维遍历地图

        row_mid = row_indices[len(row_indices) // 2]
        for i in row_indices:
            ans += (abs(row_mid - i))

        col_mid = col_indices[len(col_indices) // 2]
        for i in col_indices:
            ans += (abs(col_mid - i))

        return ans