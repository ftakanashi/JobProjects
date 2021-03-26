#!/usr/bin/env python

class Solution1:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7

        # 预处理1，得到所有pattern
        types = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k:
                        types.append([i, j, k])

        # 预处理2，得到上下两行相关矩阵
        related = [[0 for _ in range(len(types))] for _ in range(len(types))]
        for idx1, (i, j, k) in enumerate(types):
            for idx2, (x, y, z) in enumerate(types):
                if i == x or j == y or k == z: continue
                related[idx1][idx2] = 1

        # 开始dp
        dp = [[0 for _ in range(len(types))] for _ in range(n)]
        dp[0] = [1 for _ in range(len(types))]    # 第一行因为没有任何限制，所以全初始化为1
        for row in range(1, n):
            for i in range(len(types)):
                # 循环到此处是针对dp[row][i]这个位置
                # 这个位置的dp值应该是和上一行pattern在related中不冲突的所有pattern的总和
                count = 0
                for j in range(len(types)):
                    if related[i][j] == 1:
                        count += dp[row-1][j]
                dp[row][i] = count

        # 最后返回的，是终点到各种pattern的总和
        return sum(dp[-1]) % mod