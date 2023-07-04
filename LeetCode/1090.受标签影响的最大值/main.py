#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import bisect

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n = len(values)
        cnt = {}    # 标签 -> 同标签的value最大的 useLimit 个物品的value列表（排序
        for i in range(n):
            label = labels[i]
            value = values[i]
            if label not in cnt:
                cnt[label] = []
            if len(cnt[label]) < useLimit or value > cnt[label][0]:
                bisect.insort(cnt[label], value)    # 这里使用bisect.insort来保证动态插值也能始终有序
            if len(cnt[label]) > useLimit:
                cnt[label] = cnt[label][1:]    # 始终最多只保留 useLimit 个

        # 此时遗留在 cnt.values() 中的所有物品价值，理论上都是可用的。就看numWanted个数了
        all_vals = []
        for k, vals in cnt.items():
            all_vals.extend(vals)
        all_vals.sort(reverse=True)
        return sum(all_vals[:numWanted])