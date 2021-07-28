#!/usr/bin/env python
from typing import List

from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # 建立哈希表info
        info = defaultdict(list)
        for a, b in adjacentPairs:
            info[a].append(b)
            info[b].append(a)

        # 扫描找到某个头元素
        curr = None
        for k, v in info.items():
            if len(v) == 1:
                curr = k
                break

        # 从头元素开始递推构建原数组
        res, seen = [], set()    # 因为要判断某个中间元素值列表两个值中，哪个是已经出现过的值，所以用了一个seen哈希集
        while len(res) < len(info.keys()):
            res.append(curr)
            seen.add(curr)
            for nxt in info[curr]:
                if nxt in seen: continue
                curr = nxt
        return res