#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # 这两个变量分别用来表示，今后的扫描中还要还要禁言几个R和D
        R_skip, D_skip = 0, 0

        while len(set(senate)) > 1:    # 只要本轮开始人员序列还没有统一就继续扫描
            k = 0
            new_senate = ''    # 别忘了每轮要更新当前轮还没被禁言的人员序列
            '''
            这个new_senate机制也可以用双端队列来代替
            '''
            while k < len(senate):
                if senate[k] == 'R':
                    if R_skip > 0:
                        # 还有"欠着"没别禁言的R，说明当前R已经被禁言，不能发挥能力
                        R_skip -= 1
                    else:
                        # 当前R可以发挥能力，于是D需要被禁言一个人，记上一笔。同时本R也会进入下一轮（虽然R有可能会被本轮后面的D）
                        # 禁言，但只要下一轮不重置R_skip，下一轮他还是会被禁言的。
                        D_skip += 1
                        new_senate += 'R'
                else:
                    # D的视角同理
                    if D_skip > 0:
                        D_skip -= 1
                    else:
                        R_skip += 1
                        new_senate += 'D'
                k += 1
            # 一轮扫描结束。更新下一轮的名单
            # 但不更新R_skip和D_skip
            senate = new_senate
        return 'Radiant' if senate[0] == 'R' else 'Dire'


