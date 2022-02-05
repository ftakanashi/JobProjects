#!/usr/bin/env python
from typing import  List

from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        num2pos = defaultdict(list)
        for i, num in enumerate(arr):
            num2pos[num].append(i)
        queue = deque()
        queue.append((0, 0))
        seen = set([0,])
        while queue:
            pos, step = queue.popleft()
            if pos == n - 1: return step

            if arr[pos] in num2pos:
                for nxt in num2pos[arr[pos]]:
                    if nxt == pos: continue
                    queue.append((nxt, step + 1))
                    seen.add(nxt)
                num2pos.pop(arr[pos])    # 一旦走进上面循环，所有值为arr[pos]的位置都已入队，因此num2pos中的此项已经没有用了，可直接pop掉防止后续冗余计算

            if pos - 1 >= 0 and pos - 1 not in seen:
                queue.append((pos - 1, step + 1))
                seen.add(pos - 1)
            if pos + 1 < n and pos + 1 not in seen:
                queue.append((pos + 1, step + 1))
                seen.add(pos + 1)
        return -1