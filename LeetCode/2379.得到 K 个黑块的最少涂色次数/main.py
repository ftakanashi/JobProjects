#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import Counter

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt = Counter(blocks[:k])
        ans = cnt["W"]
        for i in range(k, len(blocks)):
            cnt[blocks[i]] += 1
            cnt[blocks[i-k]] -= 1
            ans = min(ans, cnt["W"])
        return ans