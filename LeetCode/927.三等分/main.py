#!/usr/bin/env python
from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        total = sum(arr)
        if total % 3 > 0: return [-1, -1]    # 先排除两种特殊情况
        if total == 0: return [0, 2]
        tgt = total // 3

        # 定位first, second, third
        first = second = third = s = 0
        for i, d in enumerate(arr):
            if d == 0: continue    # 别忘了这句，否则定位会错误
            s += d
            if s == 1: first = i
            elif s == tgt + 1: second = i
            elif s == tgt * 2 + 1: third = i

        # 开始三指针扫描
        i, j, k = first, second, third
        while k < n:
            # 以下两种情况都表示三部分的值不同，因此直接返回-1 -1
            if i == second or j == third: return [-1, -1]
            if arr[i] != arr[k] or arr[j] != arr[k]: return [-1, -1]
            i += 1
            j += 1
            k += 1
        return [i - 1, j]    # 返回最终答案
