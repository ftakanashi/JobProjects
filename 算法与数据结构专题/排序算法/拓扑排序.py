#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
拓扑排序：
参考LC.210。拓扑排序不是数组排序，而是图排序。
和一般的数组排序相比，拓扑排序有以下几个特点
1. 不一定只有一个答案。比如没有任何一条边的一个图，节点的任意一个排序都是合法的拓扑排序
2. 可能没有答案。拓扑排序算法也是查看有向图中是否有环的算法。如有环，则不存在合法拓扑排序
'''

def TopologySort(graph):
    '''
    这里我们假设graph是一个邻接表形式的图，n个节点用 0 ~ n-1 表示
    '''

    n = len(graph)
    visited = set()
    finished = set()
    res = []

    def dfs(node):
        '''
        dfs函数判断从节点node出发探索到其下一个节点，是否会成环
        '''
        if node in finished: return True    # 该节点已经结束探索，没必要重复探索
        if node in visited: return False    # 该节点之前已经开始探索，但未结束探索，说明形成环
        visited.add(node)
        for nxt in graph[node]:
            flag = dfs(nxt)
            if not flag: return False    # 一出现环，直接层层False返回回去
        # 此时所有下一个节点的探索都完成
        finished.add(node)
        res.append(node)
        return True

    for i in range(n):
        flag = dfs(i)
        if not flag: return []    # 这里比较容易忽视。当任意一个节点出发的探索探索到了环，就直接返回。
        # 否则可能从一些节点出发能够探索到合法的部分图导致最终返回结果错误

    res.reverse()    # 别忘了res中是倒序保存的
    return res