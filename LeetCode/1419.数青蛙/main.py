#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ans = 0
        cnt = [0 for _ in range(5)]
        for ch in croakOfFrogs:
            if ch == 'c':
                if cnt[4] > 0: cnt[4] -= 1    # 这步非常重要，以避免重复统计青蛙
                cnt[0] += 1
            elif ch == 'r':
                if cnt[0] == 0: return -1
                cnt[0] -= 1
                cnt[1] += 1
            elif ch == 'o':
                if cnt[1] == 0: return -1
                cnt[1] -= 1
                cnt[2] += 1
            elif ch == 'a':
                if cnt[2] == 0: return -1
                cnt[2] -= 1
                cnt[3] += 1
            elif ch == 'k':
                if cnt[3] == 0: return -1
                cnt[3] -= 1
                cnt[4] += 1
                ans = max(ans, cnt[4])

        return ans if not any(cnt[:-1]) else -1