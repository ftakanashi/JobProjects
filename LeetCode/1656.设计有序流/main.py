#!/usr/bin/env python
from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.data = [None for _ in range(n)]
        self.n = n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        ans = []
        self.data[idKey - 1] = value
        i = self.ptr
        while i < self.n and self.data[i] is not None:
            ans.append(self.data[i])
            i += 1
        if len(ans) > 0:
            self.ptr = i
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)