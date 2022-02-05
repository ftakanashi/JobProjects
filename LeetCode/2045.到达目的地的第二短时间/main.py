#!/usr/bin/env python
from typing import List

import collections
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # 建图
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        first_arrive = False    # early stop用变量
        queue = collections.deque([(1, 0)])
        F = float('inf')
        node_time = [[F, F] for _ in range(n+1)]    # 由于节点是1到n而不是0到n-1，为了后续方便，直接写n+1长度的
        node_time[1][0] = 0    # node_time[i][j]表示，到节点i的最短(j==0)和次短(j==1)时间
        while queue:
            node, curr = queue.popleft()
            if node == n:
                if first_arrive:    # 第二次搜索到终点了，可以early stop并返回
                    return curr
                else:
                    first_arrive = True    # 第一次搜索到终点，置变量为True后继续搜索

            if (curr // change) & 1 == 0:    # 考虑红绿灯影响后，计算到达下一个节点的累计时间
                nxt_time = curr + time
            else:
                nxt_time = change * ((curr // change) + 1) + time

            for nxt in graph[node]:
                # 到达下一个节点后，按规则更新node_time的最短，次短时间信息
                if nxt_time >= node_time[nxt][1]:
                    continue
                elif node_time[nxt][0] < nxt_time < node_time[nxt][1]:
                    node_time[nxt][1] = nxt_time
                elif nxt_time == node_time[nxt][0]:    # 由于是求严格次短时间，若相等则只能跳过
                    continue
                else:
                    node_time[nxt][1] = node_time[nxt][0]
                    node_time[nxt][0] = nxt_time
                queue.append((nxt, nxt_time))
        return -1