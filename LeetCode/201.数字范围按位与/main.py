#!/usr/bin/env python

class Solution1:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right: return left
        gap = right - left + 1
        ans = bit = 0
        while gap >= (2**bit + 1):    # 确定一些必然是0的低位
            bit += 1

        while bit < 32:    # 对于更高的位
            mask = (1 << bit)
            if left & mask > 0 and right & mask > 0:    # 仅当left和right的这个位都是1，最终答案的这个位才能是1
                ans = ans | mask
            bit += 1

        return ans

class Solution2:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right - 1)
        return right