#!/usr/bin/env python
from typing import List

class Solution1:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for log in logs:
            key, con = log.split(' ', 1)
            if con[0].isdigit(): digit_logs.append(log)
            else: letter_logs.append((con, key))

        res = []
        for con, key in sorted(letter_logs): res.append(f'{key} {con}')
        res.extend(digit_logs)
        return res

class Solution2:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def myorder(log: str):
            key, con = log.split(' ', 1)
            return (1, ) if con[0].isdigit() else (0, con, key)

        logs.sort(key=myorder)
        return logs