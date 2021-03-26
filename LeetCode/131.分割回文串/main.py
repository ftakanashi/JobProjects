#!/usr/bin/env python
from typing import List

class Solution1:
    def partition(self, s: str) -> List[List[str]]:

        mem = {}
        total_res = []
        n = len(s)

        def isPalin(start: int, end: int) -> bool:
            if (start, end) in mem: return mem[(start, end)]
            if start >= end: res = True
            else:
                while start < end and s[start] == s[end]:
                    start += 1
                    end -= 1
                res = start >= end
            mem[(start, end)] = res
            return res

        def dfs(start: int, res: List[str]):
            if start == n:
                total_res.append(res.copy())
                return

            for end in range(start, n):
                if isPalin(start, end):
                    subs = s[start:end+1]
                    res.append(subs)
                    dfs(end+1, res)
                    res.pop()

        dfs(0, [])
        return total_res


from functools import lru_cache as cache
class Solution2:
    def partition(self, s: str) -> List[List[str]]:

        total_res = []
        n = len(s)

        @cache
        def isPalin(start: int, end: int) -> bool:
            if start >= end: return True
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True

        def dfs(start: int, res: List[str]):
            if start == n:
                total_res.append(res.copy())
                return

            for end in range(start, n):
                if isPalin(start, end):
                    subs = s[start:end+1]
                    res.append(subs)
                    dfs(end+1, res)
                    res.pop()

        dfs(0, [])
        return total_res