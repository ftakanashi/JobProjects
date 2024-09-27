#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from collections import defaultdict

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # 构建首字母 -> 后缀映射，后缀侧是一个哈希集
        names = defaultdict(set)
        for idea in ideas:
            names[idea[0]].add(idea[1:])

        ans = 0
        for a in names:
            sa = names[a]
            for b in names:
                if a == b: continue    # 遍历所有首字母对（除了相同的情况）
                sb = names[b]
                mutual_cnt = len(sa.intersection(sb))    # 计算交集的长度
                # 除了交集部分，其余所有单词都可两两任意组合
                ans += (len(sa) - mutual_cnt) * (len(sb) - mutual_cnt)
        return ans