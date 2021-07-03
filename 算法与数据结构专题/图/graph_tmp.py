#!/usr/bin/env python

F = float('inf')
direc_graph = [
    [0, F, 5, 2, F, F, F],
    [11, 0, 4, F, F, 4, F],
    [F, 3, 0, F, 2, 7, F],
    [F, F, F, 0, 6, F, F],
    [F, F, F, F, 0, F, 2],
    [F, F, F, F, F, 0, 3],
    [F, F, F, F, F, F, 0]
]

non_direc_graph = [
    [0,  5,  11,  5,  F,  F,  F],
    [5,  0,  F,   3,  9,  F,  7],
    [11, F,  0,   7,  F,  6,  F],
    [5,  3,  7,   0,  F,  F, 20],
    [F,  9,  F,   F,  0,  F,  8],
    [F,  F,  6,   F,  F,  0,  8],
    [F,  7,  F,  20,  8,  8,  0]
]


import collections
def bfs(graph, start):
    res = []
    visited = set()
    queue = collections.deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node not in visited:
            res.append(node)
            visited.add(node)
        for nxt, edge in enumerate(graph[node]):
            if edge < F and nxt != node and nxt not in visited:
                queue.append(nxt)
    return res

import heapq
def prim(graph, start):
    n = len(graph)
    res = 0
    queue = []
    visited = set([start, ])
    for i in range(n):
        if graph[start][i] < F and i != start:
            heapq.heappush(queue, (graph[start][i], start, i))

    while queue and len(visited) < n:
        edge, a, b = heapq.heappop(queue)
        if b in visited: continue
        # res.append((a, b))
        res += edge
        visited.add(b)
        for i in range(n):
            if graph[b][i] < F and i != b and i not in visited:
                heapq.heappush(queue, (graph[b][i], b, i))
    return res

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf') for _ in range(n)]
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if dist[node] < d: continue
        dist[node] = d
        for i, nxt in enumerate(graph[node]):
            if nxt < F and i != node:
                heapq.heappush(heap, (d + nxt, i))
    return dist


def topo_sort(graph):
    res, visited, finished = [], set(), set()

    def dfs(node):
        if node in finished: return True
        if node in visited: return False
        visited.add(node)
        for i, edge in enumerate(graph[node]):
            if edge < F and i != node:
                if not dfs(i): return False
        finished.add(node)
        res.append(node)
        return True

    for i in range(len(graph)):
        if not dfs(i): return []
    res.reverse()
    return res

import copy
def floyd(graph):
    n = len(graph)
    path = copy.deepcopy(graph)
    nxt_node = [[-1 if graph[i][j] is F else j for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if path[i][j] > path[i][k] + path[k][j]:
                    path[i][j] = path[i][k] + path[k][j]
                    nxt_node[i][j] = nxt_node[i][k]

    for row in path:
        for i in row:
            print(i, end='\t')
        print('')

def main():
    floyd(non_direc_graph)

    print('=' * 10)

    n = len(non_direc_graph)
    for i in range(n):
        res = dijkstra(non_direc_graph, i)
        print('\t'.join(str(i) for i in res))

if __name__ == '__main__':
    main()