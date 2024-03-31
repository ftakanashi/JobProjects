#!/usr/bin/env python
# -*- coding:utf-8 -*-
import heapq
from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = []
        for ch, cnt in Counter(s).items():
            heapq.heappush(heap, (-ord(ch), cnt, ch))

        ans = ""
        last_ch, last_cnt = None, 0
        while heap:
            _ord, cnt, ch = heapq.heappop(heap)
            if len(ans) >= repeatLimit and last_ch == ch and last_cnt == repeatLimit:
                if not heap: break
                new_ord, new_cnt, new_ch = heapq.heappop(heap)
                ans += new_ch
                last_ch, last_cnt = new_ch, 1
                new_cnt -= 1
                if new_cnt > 0:
                    heapq.heappush(heap, (new_ord, new_cnt, new_ch))
                heapq.heappush(heap, (_ord, cnt, ch))
            else:
                ans += ch
                if ans[-1] == last_ch:
                    last_cnt += 1
                else:
                    last_ch, last_cnt = ch, 1
                cnt -= 1
                if cnt > 0:
                    heapq.heappush(heap, (_ord, cnt, ch))
        return ans