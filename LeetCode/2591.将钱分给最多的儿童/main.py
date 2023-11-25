#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # 先排除钱不够的情况
        if money < children: return -1

        # 给每人分保底的1美元
        money -= children

        # 尝试给每个人都发够8美元，即每个人补充7美元
        ans = 0
        for _ in range(children):
            # 当余额还够7美元时，发一个人
            if money >= 7:
                ans += 1
                money -= 7
            else:
                break

        # 跳出循环后，有两种可能需要将ans向下修正
        # 第一，所有人都发够了8美元且还有余额
        # 第二，中途余额不够了，此时为了避免发4美元，还需要讨论剩余未发够人数以及余额的情况
        # 以上两种可能分别对应下面if语句的两个条件
        if (money != 0 and ans == children) or (money == 3 and ans == children - 1):
            ans -= 1

        return ans