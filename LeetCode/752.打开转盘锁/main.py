#!/usr/bin/env python
from typing import List

import collections
class Solution:

    def generateNextCode(self, code: List[str]) -> List[str]:
        for i in range(4):
            for d in (1, -1):
                n = int(code[i]) + d
                if n == 10: n = 0
                elif n == -1: n = 9
                yield code[:i] + str(n) + code[i+1:]

    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set([])
        queue = collections.deque([])
        queue.append(('0000', 0))
        while len(queue) > 0:
            code, count = queue.popleft()
            if code in deadends or code in visited:
                continue
            if code == target:
                return count
            visited.add(code)
            for next_code in self.generateNextCode(code):
                queue.append((next_code, count + 1))

        return -1