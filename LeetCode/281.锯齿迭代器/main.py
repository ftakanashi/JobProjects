#!/usr/bin/env python
from typing import List

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vs = [v1, v2]
        self.m = len(self.vs)
        self.x = 0
        self.ys = [0 for _ in range(self.m)]
        # 创建一个empty哈希集，用于表示哪些行已经遍历到尾巴了
        # 通过维护这个哈希集，可以很方便地检查当前行是否该跳过以及检查hasNext
        self.empty = set([i for i, v in enumerate(self.vs) if len(v) == 0])

    def next(self) -> int:
        while self.x in self.empty:
            self.x = (self.x + 1) % self.m
        res = self.vs[self.x][self.ys[self.x]]
        self.ys[self.x] += 1
        if self.ys[self.x] == len(self.vs[self.x]):
            self.empty.add(self.x)
        self.x = (self.x + 1) % self.m
        return res

    def hasNext(self) -> bool:
        return len(self.empty) < self.m

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())