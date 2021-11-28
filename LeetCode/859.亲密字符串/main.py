#!/usr/bin/env python
from collections import defaultdict

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal): return False

        i, n = 0, len(s)    # 扫描两字符串
        pos = []    # 对应字符不同时将下标入pos
        while i < n:
            if s[i] != goal[i]:
                if len(pos) == 2: return False    # 若有超过两处不同，直接返回False
                pos.append(i)
            i += 1

        if len(pos) == 0:    # 两者完全相等时，看是否有字母重复出现。只要有就True
            counter = defaultdict(int)
            for ch in s:
                counter[ch] += 1
                if counter[ch] == 2: return True
            return False
        elif len(pos) == 1:    # 有且仅有一处不同，直接False
            return False
        else:
            return s[pos[0]] == goal[pos[1]] and s[pos[1]] == goal[pos[0]]    # 最普遍情况