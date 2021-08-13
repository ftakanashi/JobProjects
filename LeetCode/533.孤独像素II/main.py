#!/usr/bin/env python
from typing import List
from collections import defaultdict

class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        m, n = len(picture), len(picture[0])
        row_ptn_cnt = defaultdict(int)
        row_ptn_bc = defaultdict(int)

        # 预处理记录行pattern信息
        for row in picture:
            rs = ''.join(row)
            row_ptn_cnt[rs] += 1
            if rs not in row_ptn_bc:
                row_ptn_bc[rs] += rs.count('B')

        # 预处理记录列信息
        cols = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    cols[j] += 1

        ans = 0
        for row_ptn in row_ptn_cnt:
            if row_ptn_cnt[row_ptn] == target and row_ptn_bc[row_ptn] == target:
                for j in range(n):
                    if row_ptn[j] == 'B' and cols[j] == target:
                        # 只有那些行pattern恰好有target个且pattern内恰好有target个B
                        # 且这些B所在的列中，除了行pattern以外行其他没有B的情况，才符合条件，予以收割
                        ans += target
        return ans