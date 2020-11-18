#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import collections
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 构建值和排序key的对应关系
        order = collections.defaultdict(lambda: float('inf'))
        for i, n in enumerate(arr2):
            order[n] = i

        def partition(lst, order, left, right):
            if left >= right: return
            i = d = left + 1
            while d <= right:
                if order[lst[d]] < order[lst[left]] or \
                        (order[lst[d]] == float('inf') and order[lst[left]] == float('inf')
                         and lst[d] < lst[left]):
                    lst[d], lst[i] = lst[i], lst[d]
                    i += 1
                d += 1

            i -= 1
            lst[left], lst[i] = lst[i], lst[left]

            partition(lst, order, left, i - 1)
            partition(lst, order, i + 1, right)

        partition(arr1, order, 0, len(arr1) - 1)
        return arr1