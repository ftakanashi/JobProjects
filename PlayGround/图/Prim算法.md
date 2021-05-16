# Prim算法
首先记住，Prim和Kruskal算法一样，都是解决最小生成树问题的。

即，给出一些节点和一些边的权值，要求生成一个最小生成树，
使得各个节点在处于同一个连通分量的前提下，使用的所有边的权值最小。

Kruskal算法是"基于边的视角"的。从小到大优先拿权值最小的边入图，当然如果某两个点在使用某条边前就已经在一个连通分量中了，自然就没必要加这个边了。

Prim算法则是"基于节点的视角"的。
在构建生成树的过程中，总有一些已经进入树的节点 和 通过一些侯选边与这些节点相连的还未进入树的节点。

以侯选边权值作为权重，用堆维护这些边。
每一时刻，我都选择侯选边中权值最小的那条，将那条边连到的未入树的节点入树。
最后，以新入的这个节点为起点，将从其出发的所有边入堆。
注意，这里对入堆的边还有一个要求，就是连向的点不能在树中，否则就是连回头路，没必要。

# 具体代码
还是以邻接矩阵实现的无向图(图例见Python算法书P.244)作为示例：
```python
F = float('inf')
non_direc_graph = [
    [0, 5, 11, 5, F, F, F],
    [5, 0, F, 3, 9, F, 6],
    [11, F, 0, 7, F, 6, F],
    [5, 3, 7, 0, F, F, 20],
    [F, 9, F, F, 0, F, 8],
    [F, F, 6, F, F, 0, 8],
    [F, 6, F, 20, 8, 8, F]
]
```

prim算法的代码如下：
```python
import heapq
F = float('inf')
def prim(graph, start):
    n = len(graph)
    res = []
    queue = []
    visited = set([start, ])
    for i in range(n):
        if graph[start][i] < F and i != start:
            heapq.heappush(queue, (graph[start][i], start, i))
    
    while queue and len(visited) < n:
        edge, a, b = heapq.heappop(queue)
        if b in visited: continue
        res.append((a, b))
        visited.add(b)
        for i in range(n):
            if graph[b][i] < F and i != b and i not in visited:
                heapq.heappush(queue, (graph[b][i], b, i))
    return res
```
当然上面res收割的是各个边，要是换成加等权值就是求最小生成树的权值和了。

# 分析
设图为`G = (E, V)`。
时间复杂度是`O(ElogE)`。