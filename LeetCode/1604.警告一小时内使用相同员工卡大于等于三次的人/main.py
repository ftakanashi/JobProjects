#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from functools import lru_cache as cache

from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        @cache
        def parseTime(time_str):
            hour, minute = time_str.split(":")
            return int(hour) * 60 + int(minute)

        keyInfo = [(name, parseTime(time)) for name, time in zip(keyName, keyTime)]
        keyInfo.sort(key=lambda x: x[1])

        times = defaultdict(list)
        ans = set()
        for name, time in keyInfo:
            if len(times[name]) > 1 and time - times[name][-2] <= 60:
                ans.add(name)
            times[name].append(time)

        return sorted(ans)