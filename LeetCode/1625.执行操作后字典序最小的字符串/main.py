#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans = s
        rotated = set()
        s = list(s)

        for _ in range(len(s)):
            s = s[-b:] + s[:-b]    # 一个轮转后的基础模板
            if "".join(s) in rotated:    # 通过哈希集过滤掉一部分重复的处理
                continue
            rotated.add("".join(s))

            for j in range(10):   # 尝试给每个奇数位累加，最多10次

                for k in range(1, len(s), 2):
                    s[k] = str((int(s[k]) + a) % 10)

                if b & 1:    # 若b是奇数，则还需要考虑每个偶数位累加，最多10次
                    for p in range(10):
                        for k in range(0, len(s), 2):
                            s[k] = str((int(s[k]) + a) % 10)
                        ans = min(ans, "".join(s))

                else:    # 若b是偶数，偶数为不可能被累加处理到，所以可以直接跳过
                    ans = min(ans, "".join(s))

        return ans