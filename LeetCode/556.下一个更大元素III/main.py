#!/usr/bin/env python
import bisect

class Solution:
    def nextGreaterElement(self, n: int) -> int:

        # 先数字化各个位
        digits = []
        while n > 0:
            digits.append(n % 10)
            n = n // 10
        digits.reverse()

        # 找到末尾递减序列的分界点pos
        pos = -1
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] < digits[i+1]:
                pos = i
                break
        if pos == -1: return -1    # 若pos保持-1，说明原数整个就是一个递减的序列，此时无更大的数字，返回-1

        # 从末尾递减序列中找到比分界点数字大且尽量小的数字
        tail = digits[pos+1:]
        tail.reverse()
        insert_i = bisect.bisect(tail, digits[pos])

        # 互换两个数字，并且将递减序列重新嵌回原数字
        tmp = tail[insert_i]
        tail[insert_i] = digits[pos]
        digits[pos] = tmp
        digits[pos+1:] = tail

        # 基于各个位置的数重建答案，注意边界判断
        ans = 0
        BOUND = (2**31 - 1) // 10
        for digit in digits:
            if ans > BOUND or (ans == BOUND and digit > 7): return -1
            ans = ans * 10 + digit
        return ans