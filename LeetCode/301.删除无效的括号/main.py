#!/usr/bin/env python
from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def check(ss):
            flag = 0
            for ch in ss:
                if ch == '(': flag += 1
                elif ch == ')': flag -= 1
                if flag < 0: return False

            return flag == 0

        queue = deque([s, ])
        seen = set()
        ans = []
        max_len = -1
        while queue:
            cand = queue.popleft()
            if len(cand) < max_len or cand in seen: continue
            seen.add(cand)
            if check(cand):
                ans.append(cand)
                max_len = max(len(cand), max_len)    # 别忘了这步，可以帮助后续搜索提前终止
            for i in range(len(cand)):
                new_s = cand[:i] + cand[i+1:]
                queue.append(new_s)
        return ans