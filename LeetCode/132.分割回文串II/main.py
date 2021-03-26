#!/usr/bin/env python
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # 预处理s，获取判断任意子串回文性质的矩阵palin
        palin = [[True for _ in range(n)] for _ in range(n)]
        for diff in range(1, n):
            # 从对角线开始向右上一层一层扫描。每层的标志是j-i的差diff
            i = 0
            j = diff
            while j < n:
                palin[i][j] = palin[i+1][j-1] and s[i] == s[j]
                i += 1
                j = i + diff

        # 设置dp数组，逐个扫描各个位置为右边界时的最小切割次数
        dp = [i for i in range(n)]
        for j in range(n):
            if palin[0][j]: dp[j] = 0
            else:
                for i in range(j):
                    if palin[i+1][j]:
                        dp[j] = min(dp[j], dp[i]+1)

        return dp[-1]