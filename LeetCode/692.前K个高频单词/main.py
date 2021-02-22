#!/usr/bin/env python

from typing import List

import collections
class Solution1:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        res = []
        for w in sorted(counter, key=lambda x: (-counter[x], x)):
            res.append(w)
            if len(res) == k: return res

import heapq
class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        kvs = [(-cnt, w) for w, cnt in counter.items()]
        heapq.heapify(kvs)
        res = []
        for _ in range(k):
            _, w = heapq.heappop(kvs)
            res.append(w)
        return res