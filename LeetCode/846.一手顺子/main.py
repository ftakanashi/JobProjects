#!/usr/bin/env python
from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False
        hand.sort()
        counter = Counter(hand)

        i = 0
        while i < n:    # 以i为指针扫描排序后的数组
            i += 1
            # 若扫描到的数字计数已经归零，说明这种牌已经全部被用于其他顺子的构建，无需考虑其作为起始的顺子的可能性了
            if counter[hand[i]] > 0:
                for h in range(hand[i], hand[i] + groupSize):
                    # 构建顺子，即，将顺子中的各个牌的计数值减去1
                    counter[h] -= 1
                    if counter[h] < 0: return False    # 使用了已经归零的牌，顺子不成立，直接返回False
        return True