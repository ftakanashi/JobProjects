#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List, Tuple

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def partition(arr: List[Tuple[int, int]], left: int, right: int):
            if left >= right: return
            i = d = left + 1
            while d <= right:
                # 两个维度分两种条件，第一种如果1的个数比较少，第二种如果1的个数相同但是本身值比较小，就交换到左区
                if arr[d][0] < arr[left][0] or \
                  (arr[d][0] == arr[left][0] and arr[d][1] < arr[left][1]):
                    arr[i], arr[d] = arr[d], arr[i]
                    i += 1
                d += 1
            i -= 1
            arr[i], arr[left] = arr[left], arr[i]
            partition(arr, left, i - 1)
            partition(arr, i + 1, right)

        new_arr = [self.countOne(n) for n in arr]

        partition(new_arr, 0, len(new_arr) - 1)
        return [p[1] for p in new_arr]
        # return [p[1] for p in sorted(new_arr)]    # 如果使用系统内建排序方法，直接用这行即可。

    def countOne(self, n: int) -> Tuple[int, int]:
        '''
        统计二进制下1的个数
        '''
        count = 0
        orig_n = n
        while n > 0:
            n = n & (n - 1)
            count += 1

        return count, orig_n    # 同时返回原值，方便后续排序