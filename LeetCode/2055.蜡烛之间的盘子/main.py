#!/usr/bin/env python
from typing import List

from bisect import bisect_left
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        presum = []
        curr = 0
        # 构建前缀和
        for i in range(n):
            if s[i] == "|":
                curr += 1
            presum.append(curr)

        ans = []
        for start, end in queries:
            total = end - start + 1    # 区间内所有盘子和蜡烛的总数
            if total <= 2 or presum[start] == presum[end]:
                ans.append(0)    # 若区间长度本身小于等于2或者区间全是盘子，那么直接是0
                continue
            total -= (presum[end] - presum[start])
            # 到这里，total中已经去除了所有蜡烛的数量（不包括左端点恰好是蜡烛的情况
            if s[start] == "|":
                total -= 1    # 左端点恰好是蜡烛时，再去除左端点蜡烛即可
            else:
                # 左端点不是蜡烛时，进一步去除所有左侧未被蜡烛包裹的盘子数量
                total -= (bisect_left(presum, presum[start] + 1) - start)

            # 无论如何右侧未被包裹的盘子都可以通过如下方式求
            total -= (end - bisect_left(presum, presum[end]))

            ans.append(total)
        return ans