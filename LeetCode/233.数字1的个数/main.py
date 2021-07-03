#!/usr/bin/env python
class Solution:
    def countDigitOne(self, n: int) -> int:
        ans, base = 0, 1
        orig_n = n    # 为了遍历过程中能够实时获得已扫描的部分，额外保存一下原n
        while n > 0:
            digit = n % 10
            rest = n // 10    # 未扫描部分
            scanned = orig_n % base    # 已扫描部分

            # 按照规律公式写代码
            if digit > 1:
                ans += (rest + 1) * base
            elif digit == 1:
                ans += (rest + 1) * base - ((base - 1) - scanned)
            else:
                ans += rest * base

            n = rest
            base *= 10    # 别忘了更新base

        return ans