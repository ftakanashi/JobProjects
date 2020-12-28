#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            pattern = ''.join(sorted(s))
            if pattern not in m:
                m[pattern] = [s, ]
            else:
                m[pattern].append(s)
        return list(m.values())