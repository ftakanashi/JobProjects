#!/usr/bin/env python
from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        for pos in range(len(bits) - 2, -2, -1):    # 这里利用了Python下标-1恰好指的是末尾元素这个特点，遍历n-2到-1的所有值
            if bits[pos] == 0:
                return (len(bits) - pos - 2) & 1 == 0    # 括号里的-2其实也可以不写，因为减不减奇偶性是不变的