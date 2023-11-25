#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from collections import Counter

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        cnt = Counter()
        for start, end in flowers:
            cnt[start] += 1
            cnt[end + 1] -= 1

        ans = [0 for _ in range(len(people))]

        flower = 0
        times = list(sorted(cnt))
        i = 0
        for p, j in sorted(zip(people, range(len(people)))):
            while i < len(times) and times[i] <= p:
                flower += cnt[times[i]]
                i += 1
            if i == len(times): break
            if times[i] >= p:
                ans[j] = flower

        return ans