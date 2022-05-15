#!/usr/bin/env python
from typing import List
from collections import Counter
from functools import lru_cache as cache

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)

        @cache
        def dfs(mask):
            if mask == 0: return 0    # 所有target中字母都被填充的情况，可以直接返回0
            ans = float('inf')
            for sticker in stickers:    # 遍历所有sticker
                counter = Counter(sticker)
                rest = mask    # 由于int是不可变类型，所以用rest来代替mask被更新
                for i, ch in enumerate(target):
                    if (rest >> i) & 1 > 0 and counter[ch] > 0:    # 只有rest中位是1，且counter中也还有存货才能执行填充
                        counter[ch] -= 1
                        rest = rest ^ (1 << i)
                if rest < mask:    # 若rest剩余的部分小于mask，说明选取当前这个sticker至少是有作用的
                    ans = min(ans, dfs(rest) + 1)    # 这里 +1 就是指选用了当前sticker的情况
            return ans

        res = dfs((1 << n) - 1)
        return res if res < float('inf') else -1