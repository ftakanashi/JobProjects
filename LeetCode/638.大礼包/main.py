#!/usr/bin/env python
from typing import List
from functools import lru_cache as cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        valids = []

        for spec in special:    # 过滤掉一些不合算的礼包
            if sum(spec[i] * price[i] for i in range(n)) > spec[-1]:
                valids.append(spec)

        @cache
        def dfs(rest):
            if sum(rest) == 0: return 0
            ans = sum(rest[i] * price[i] for i in range(n))    # 基准最低价，即只买单品不买礼包的情况
            for spec in valids:    # 依次尝试购买礼包
                spec_price = spec[-1]
                # 检查当前礼包是否会超商品数限制
                exceed_flag = False
                for i in range(n):
                    if spec[i] > rest[i]:
                        exceed_flag = True
                        break
                if exceed_flag: continue

                # 尝试买礼包可能会减少支出，取其小者即可。
                ans = min(ans, spec_price + dfs(tuple(rest[i] - spec[i] for i in range(n))))

            return ans

        return dfs(tuple(needs))