#!/usr/bin/env python

from typing import List
from functools import lru_cache as cache

class Solution1:
    def maxLength(self, arr: List[str]) -> int:
        sets = [set(a) for a in arr]    # 预处理哈希集
        invalid_indices = set()
        for i, s in enumerate(sets):
            if len(s) < len(arr[i]): invalid_indices.add(i)    # 找出本身就非法的字符串

        @cache
        def dfs(start, string):
            if start == len(arr): return len(string)
            str_set = set(string)
            ans = len(string)
            for i in range(start, len(arr)):
                # 若arr[i]本身就非法或者其与当前已经串联出来的string有重复字符，直接不选用
                if i in invalid_indices or sets[i].intersection(str_set): continue
                ans = max(ans, dfs(i+1, string + arr[i]))
            return ans

        return dfs(0, '')

class Solution2:
    def maxLength(self, arr: List[str]) -> int:
        counter = 0
        masks = []
        for a in arr:
            mask = 0
            for ch in a:
                ch_num = ord(ch) - 97
                if (mask >> ch_num) & 1 == 1:
                    mask = 0
                    break
                mask = mask | (1 << ch_num)
            masks.append(mask)

        # @cache    # 不能用cache！！！
        def dfs(start):
            nonlocal counter
            ans = bin(counter).count('1')
            if start == len(arr): return ans
            for i in range(start, len(arr)):
                if counter & masks[i] > 0: continue
                counter = counter | masks[i]
                ans = max(ans, dfs(i + 1))
                counter = counter ^ masks[i]

            return ans

        return dfs(0)