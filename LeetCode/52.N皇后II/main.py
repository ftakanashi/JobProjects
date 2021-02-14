#!/usr/bin/env python

class Solution:
    def totalNQueens(self, n: int) -> int:

        def dfs(i: int, col: int, diff_diag: int, sum_diag: int):
            if i == n: return 1
            count = 0
            for j in range(n):
                n_j = 1 << j
                n_sum_diag = 1 << (i + j)
                n_diff_diag = 1 << (i - j + n - 1)    # 由于i - j可能是负数，直接将其转化为从-(n-1)作为0开始的序数
                if col & n_j > 0 or diff_diag & n_diff_diag > 0 or sum_diag & n_sum_diag > 0:
                    continue

                count += dfs(i+1, col|n_j, diff_diag|n_diff_diag, sum_diag|n_sum_diag)

            return count

        return dfs(0, 0, 0, 0)