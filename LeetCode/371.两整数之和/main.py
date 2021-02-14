#!/usr/bin/env python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 2**32
        MAX_INT = 2**31 - 1
        MIN_INT = MAX_INT + 1
        if b == 0:
            # 第二个模拟点，如果输出是负数那么要手动转化
            return a if a <= MAX_INT else -(((a % MIN_INT) - 1) ^ MAX_INT)
            # return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)    # 第二种转化负值的办法

        # 第一个要模拟点，都对MASK取余从而保证计算有效位数始终只有32位
        res = (a ^ b) % MASK
        carry = ((a & b)<< 1) % MASK
        return self.getSum(res, carry)