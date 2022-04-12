#!/usr/bin/env python
from typing import List
from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if len(bank) == 0: return -1    # bank无内容情况的优化
        bank = set(bank)
        queue = deque()
        queue.append((start, 0))
        chars = "ACGT"
        seen = set()
        while queue:
            seq, time = queue.popleft()
            seen.add(seq)

            for i, ch in enumerate(seq):
                for new in chars:
                    if ch == new: continue
                    new_seq = seq[:i] + new + seq[i+1:]
                    if new_seq in seen or new_seq not in bank: continue
                    if new_seq == end: return time + 1
                    queue.append((new_seq, time + 1))
        return -1