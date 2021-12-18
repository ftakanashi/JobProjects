#!/usr/bin/env python
from typing import List

import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = [[t, d] for t, d in courses if t <= d]
        courses.sort(key=lambda x: x[1])    # 第一次贪心 排序

        selected = []
        total = 0
        for t, d in courses:
            if total + t <= d:    # 当前累计时间还没超过deadline时，放心大胆选课就是了
                heapq.heappush(selected, (-t, d))
                total += t
            elif selected and -selected[0][0] > t:    # 否则，就需要尝试替换课程
                tmp = heapq.heappop(selected)
                heapq.heappush(selected, (-t, d))
                total -= -tmp[0]
                total += t

        return len(selected)