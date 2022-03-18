#!/usr/bin/env python
from typing import List

from collections import defaultdict, Counter
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # 用哈希表表征树
        tree = defaultdict(list)
        for i, p in enumerate(parents):
            tree[p].append(i)

        node_scale = {}    # 记录每个节点为根节点的子树的节点数目，不包括叶节点

        def dfs(node):
            scale = [0, 0]
            if len(tree[node]) == 0:    # 叶子节点
                return 1
            elif len(tree[node]) == 1:    # 只有一个子树，此时倒是不用关心是左子树还是右子树，这不影响其后的计算
                scale[0] = dfs(tree[node][0])
            else:
                scale[0] = dfs(tree[node][0])
                scale[1] = dfs(tree[node][1])
            node_scale[node] = scale
            return sum(scale) + 1    # +1是为了计数node本身

        dfs(0)
        n = len(parents)
        counter, max_ans = Counter(), -1
        for i in range(n):    # 遍历每个节点
            if i in node_scale:     # 非叶子节点的情况
                # 下面的乘法为了避免乘出0，乘以的因子下限都是1
                new = 1
                new *= max(node_scale[i][0], 1)
                new *= max(node_scale[i][1], 1)
                new *= max(n - sum(node_scale[i]) - 1, 1)
            else:    # 叶子节点的情况，其分数必然是n-1
                new = n - 1
            counter[new] += 1
            max_ans = max(new, max_ans)
        return counter[max_ans]