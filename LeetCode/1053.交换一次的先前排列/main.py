#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]: continue

            j = n - 1
            # 这里并不用对 j > 0 做出限制，因为最多到 i+1 为止，肯定会有一个 arr[j] < arr[i] 。
            while arr[j] >= arr[i] or arr[j] == arr[j - 1]:
                j -= 1

            arr[i], arr[j] = arr[j], arr[i]
            break

        return arr