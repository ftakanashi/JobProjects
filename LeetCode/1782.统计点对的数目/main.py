#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import bisect
from collections import Counter

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:

        # 预处理阶段
        degree = [0 for _ in range(n)]    # 各个节点的度数，注意节点是从1开始编号，这里下标是从0开始
        cnt = Counter()    # 保存任意两节点间的直连边数
        for a, b in edges:
            a, b = a - 1, b - 1    # 修正下标编号
            if a > b: a, b = b, a
            degree[a] += 1
            degree[b] += 1
            cnt[(a, b)] += 1    # 始终固定小值在左侧，以免出现 (1,2) 和 (2,1) 这样的重复计数

        # 这里排序必须要制作副本
        # 因为degree中没有显式记录度数和点的对应关系，只有下标这层关系。一旦重新排序后下标信息就没了
        sort_degree = sorted(degree)
        ans = []
        for query in queries:
            # 针对每个query单独平行求解

            # 扫描所有节点（但是按照度数排序后的顺序扫描，不一定按原下标从0开始由小到大顺序扫描
            tmp = 0
            for i, d in enumerate(sort_degree):
                # 这里进行二分查找的时候还有一个需要注意的小细节。
                # 遍历当前节点的下标是i，但是如果扫描范围是全局的话，那么那些下标小于i且满足要求的点也会被算进去
                # 这显然是重复计算了（之前的遍历中已经算过了
                # 解决方法是在bisect方法中添加lo参数为i+1，这样就只会扫描i右边的点
                j = bisect.bisect(sort_degree, query - d, i + 1)
                tmp += (n - j)   # j下标对应的点以及其右边所有度数更大的点，都可能和当前遍历的点形成符合要求的点对

            # 等上面这个循环完成后
            # 再统一检查一遍所有可能的重复边，减去相应点对数量即可
            for (a, b), cnt_val in cnt.items():
                if degree[a] + degree[b] > query and degree[a] + degree[b] - cnt_val <= query:
                    tmp -= 1

            ans.append(tmp)

        return ans

    """
    写在最后
    这题答案是照抄官答的…估计自己想的话很难想到。而且想到之后，为了排除重复边的影响，
    很容易就会想 能不能在收割答案的时候把点对记录下来。
    但是这里最终的做法，就体现一个大道至简。因为点对的组合是完全自由的，不要求两个点之间有顺序或者有连接之类的。
    那么就是可以，暴力计算所有计数（只要确保计算时不重复计数点对），然后再统一扣除重复边造成的影响即可。
    """