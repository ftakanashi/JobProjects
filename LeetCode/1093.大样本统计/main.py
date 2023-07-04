#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = float("inf")
        maximum = float("-inf")
        total_cnt = 0
        max_cnt = 0
        mode = None
        s = 0
        for i, cnt in enumerate(count):
            if cnt > 0:
                minimum = min(minimum, i)
                maximum = max(maximum, i)
            total_cnt += cnt
            if cnt > max_cnt:
                mode = i
                max_cnt = cnt
            s += (i * cnt)
        mean = s / total_cnt

        # 第一次遍历完成后，得到 minimum, maximum, mean, mode

        median = None
        mid = total_cnt // 2
        seen = 0
        i = 0
        if total_cnt & 1 == 0:
            while i < 256:
                seen += count[i]
                if seen == mid:
                    j = i + 1
                    while j < 256 and count[j] == 0:
                        j += 1
                    median = (i + j) / 2
                    break
                elif seen > mid:
                    median = i
                    break
                i += 1
        else:
            mid += 1
            while i < 256:
                seen += count[i]
                if seen >= mid:
                    median = i
                    break
                i += 1

        # 第二次遍历完成后得到median

        return [minimum, maximum, mean, median, mode]
