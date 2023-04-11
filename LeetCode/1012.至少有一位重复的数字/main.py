#!/usr/bin/env python
# -*- coding:utf-8 -*-

from functools import lru_cache as cache

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = [int(ch) for ch in str(n)]    # 将 n 拆分成各个位的数字

        @cache
        def dfs(pos, used, tight):
            if pos == len(digits):    # 只要能填到超过digits长度，说明必然存在一个合法答案，返回1
                return 1

            # 通过tight决定当前填写数字的上限
            upper_limit = digits[pos] if tight else 9

            ans = 0
            for num in range(upper_limit + 1):
                # num已经被使用过了
                if (1 << num) & used > 0: continue

                # 下一轮dfs的tight按下式决定（不能超过限制）
                new_tight = tight and num == digits[pos]

                # 下一轮的used按下式决定（考虑前导零的情况）
                if num == 0 and used == 0:
                    new_used = 0
                else:
                    new_used = used | (1 << num)

                ans += dfs(pos + 1, new_used, new_tight)

            return ans

        # 最后别忘了题目要求的和dfs出来的不是同一个东西
        return n - dfs(0, 0, True) + 1