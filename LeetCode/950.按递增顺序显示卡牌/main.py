#!/usr/bin/env python
from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        indices = deque(range(n))
        processed = []    # 构建操作一定次数后的下标序列
        while indices:
            processed.append(indices.popleft())
            if indices:
                indices.append(indices.popleft())

        ans = [0 for _ in range(n)]
        j = 0
        sort_deck = list(sorted(deck))
        for i in processed:    # 根据下标序列和排序号的牌堆，进行原序列的构建
            ans[i] = sort_deck[j]
            j += 1

        return ans
