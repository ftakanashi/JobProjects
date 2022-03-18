#!/usr/bin/env python
from typing import List

from collections import Counter
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        n = len(s)
        counter = Counter(s)
        center = ""    # 声明成空串而不是None，利于后面的代码简化
        for ch in counter:
            if counter[ch] & 1 == 1:
                if center: return []    # 计数值是奇数的字母不止一个，直接返回空列表
                else: center = ch

        stack = [None for _ in range(n // 2)]    # 进行DFS回溯处理的，回文串前半段
        if center: counter[center] -= 1    # 若有center，就先将其计数值减去1

        ans = []
        def dfs(pos):
            if pos == len(stack):
                ans.append("".join(stack) + center + "".join(reversed(stack)))    # 构建回文串
                return
            for ch in counter:
                if counter[ch] == 0: continue
                counter[ch] -= 2    # 别忘了一口气要减去2
                stack[pos] = ch
                dfs(pos + 1)
                stack[pos] = None    # 回溯复原
                counter[ch] += 2

        dfs(0)
        return ans