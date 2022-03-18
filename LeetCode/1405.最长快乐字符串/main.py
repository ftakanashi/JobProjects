#!/usr/bin/env python

import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for cnt, ch in [(a, "a"), (b, "b"), (c, "c")]:
            if cnt > 0:
                heapq.heappush(heap, (-cnt, ch))

        ans = ""
        while heap:
            cnt, ch = heapq.heappop(heap)
            tmp = None
            if len(ans) > 1 and ans[-2] == ans[-1] == ch:
                if len(heap) == 0: break
                tmp = (cnt, ch)
                cnt, ch = heapq.heappop(heap)
            ans += ch
            if cnt < -1:    # 若cnt是-1，则下面+1后直接变0了，就无必要继续入堆
                heapq.heappush(heap, (cnt + 1, ch))
            if tmp:
                heapq.heappush(heap, tmp)

        return ans