#!/usr/bin/env python
from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0 for _ in range(n)]
        for log in logs:
            pid, act, time = log.split(":")
            pid, time = int(pid), int(time)

            if act == "start":
                stack.append((pid, time))
            else:
                loss = 0
                while type(stack[-1]) is int:
                    loss += stack.pop()
                _, start_time = stack.pop()
                total = time - start_time + 1
                res[pid] += (total - loss)
                stack.append(total)

        return res