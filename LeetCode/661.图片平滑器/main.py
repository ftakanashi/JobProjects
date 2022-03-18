#!/usr/bin/env python
from typing import List

import itertools
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])

        # 构建二维前缀和
        presum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                presum[i][j] = presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1] + img[i-1][j-1]
        presum = [[presum[i][j] for j in range(1, n+1)] for i in range(1, m+1)]

        # 扫描每个格子，填充ans
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                up = left = diag = 0
                if i - 2 >= 0:    # 若i-2越界，则up是0
                    up = presum[i-2][min(j+1, n-1)]
                if j - 2 >= 0:    # 同理，j-2越界的话left也是0
                    left = presum[min(i+1, m-1)][j-2]
                if i - 2 >= 0 and j - 2 >= 0:
                    diag = presum[i-2][j-2]
                s = presum[min(i+1,m-1)][min(j+1,n-1)] - left - up + diag    # s是(i,j)格子为中心的九宫格的和

                area = 0
                for a, b in itertools.product([i-1, i, i+1], [j-1, j, j+1]):
                    if 0 <= a < m and 0 <= b < n: area += 1    # 统计周边有效格子数

                ans[i][j] = s // area

        return ans