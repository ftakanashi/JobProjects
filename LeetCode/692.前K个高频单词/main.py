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

class Entry:
    def __init__(self, cnt, word):
        self.cnt = cnt
        self.word = word

    def __gt__(self, other):
        if other.cnt != self.cnt:
            return self.cnt > other.cnt
        else:
            return self.word < other.word

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        for word, cnt in counter.items():
            e = Entry(cnt, word)
            if len(heap) < k:
                heapq.heappush(heap, e)
            elif len(heap) == k and e > heap[0]:
                heapq.heapreplace(heap, e)    # heappop + heappush操作可以用heapreplace代替

        # 整理堆中信息并收割结果返回
        res = []
        prev = heap[0].cnt
        tmp = []
        while heap:
            entry = heapq.heappop(heap)
            cnt, word = entry.cnt, entry.word
            if cnt != prev:
                prev = cnt
                tmp.reverse()
                res = tmp + res
                tmp = []
            tmp.append(word)

        tmp.reverse()
        res = tmp + res
        return res