#!/usr/bin/env python
from typing import List

from collections import defaultdict
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # 先将所有出入楼一致的项剔除，并且计数
        filtered = []
        ans = 0
        for a, b in requests:
            if a == b:
                ans += 1
            else:
                filtered.append([a, b])
        requests = filtered

        change = defaultdict(int)

        def dfs(pos, ok_req):
            if pos == len(requests):
                return ok_req if len(change) == 0 else -1

            flag = 0
            src, tgt = requests[pos]
            flag = max(flag, dfs(pos + 1, ok_req))
            change[src] -= 1
            if change[src] == 0: change.pop(src)
            change[tgt] += 1
            if change[tgt] == 0: change.pop(tgt)
            flag = max(flag, dfs(pos + 1, ok_req + 1))
            change[src] += 1
            if change[src] == 0: change.pop(src)
            change[tgt] -= 1
            if change[tgt] == 0: change.pop(tgt)
            return flag

        return ans + dfs(0, 0)