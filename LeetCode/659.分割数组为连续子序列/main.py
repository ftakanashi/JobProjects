#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import collections
import heapq

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = collections.defaultdict(list)
        for n in nums:
            if len(mp[n-1]) == 0:
                # 如果当前子序列池中没有合适的子序列可以用来append
                # 只能新建一个长度为1的子序列
                heapq.heappush(mp[n], 1)
            else:
                length = heapq.heappop(mp[n-1])    # 选出候选子序列中长度最小的
                heapq.heappush(mp[n], length + 1)    # 长度+1，并且由于末尾数变化所以变更子序列池

        for n, h in mp.items():
            if len(h) > 0 and heapq.heappop(h) < 3:    # 只要看每种末尾数子序列最短的有没有小于3即可
                return False
        return True


        # 只记录长度信息优化后的算法
        # for n in nums:
        #     if len(mp[n-1]) == 0:
        #         mp[n].append(1)
        #     else:
        #         min_i, min_len = -1, float('inf')
        #         for i, sub_len in enumerate(mp[n-1]):
        #             if sub_len < min_len:
        #                 min_i, min_len = i, sub_len
        #         mp[n].append(min_len + 1)
        #         del mp[n-1][min_i]

        # for n, subseq_lens in mp.items():
        #     if len(subseq_lens) > 0 and min(subseq_lens) < 3:
        #         return False
        # return True


        # 哈希表优化后的算法：
        # for n in nums:
        #     if len(mp[n-1]) == 0:
        #         mp[n].append([n,])
        #     else:
        #         min_i = -1
        #         min_len = float('inf')
        #         for i, sub in enumerate(mp[n-1]):
        #             if (sub_len:=len(sub)) < min_len:
        #                 min_i = i
        #                 min_len = sub_len
        #         mp[n].append(mp[n-1][min_i] + [n,])
        #         del mp[n-1][min_i]

        # for n, subseqs in mp.items():
        #     for subseq in subseqs:
        #         if len(subseq) >0 and len(subseq) < 3: return False

        # return True