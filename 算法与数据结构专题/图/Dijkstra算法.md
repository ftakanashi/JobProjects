## 单源最短路径问题
给出一个（无向或者有向都可）图以及其所有边的权值。

给定图中的一个节点，要求从这个节点出发到各个节点的最短路径（权值和）。

因为这是一个"一对多"的问题，所以也被称为单源最短路径问题。

## Dijkstra算法
Dijkstra算法基于贪心思想。
首先，既然你要我求从一个点出发到各个点的最短路径。
那么我就初始化一个dist数组保存这些信息。所有值可以初始化为`float('inf')`。

然后，开始探索路径。
在探索路径的时候，有这么一个思想：优先探索当前可以用最小代价到达的节点。
更形象地说，图中的节点被分成已经探索过的，下一个探索的备选的，以及还未探索过的三部分。

所谓的备选的，就是从当前已经探索过的节点们出发，可以到达的节点。
注意备选的不仅仅是节点，还有从开始节点到该节点的cost。

这样，我们只要每次都从备选集合中选出这个cost最小的，这就是当前可用最小代价到达的节点了。
我们可以将这个cost记录到dist数组中。
然后我们还需要将这个与这个节点相连的节点以及累加的cost成对地放进备选集合。

注意这里有个"走回头路"的问题。Dijkstra算法中不需要额外维护visited之类的结构来看某个节点是否已经处理过。
因为一旦某个节点处理过了，其dist数组中的对应项一定就不是无穷大了。
同时，其实你走了回头路，累加的cost肯定比已经保存在dist中的大了，对于挑出的最小cost都比目前dist中的大的情况，直接continue掉即可。
>注意，这里默认所有边权值都是正的。如果是负的，那么"累加的cost肯定比已经保存在dist中的大了"这句话就不成立了。

Talk is cheap. 下面给出一个基于邻接矩阵实现的图的Dijkstra算法代码：
```python
def dijkstra(graph, start):
    dist = [float('inf') for _ in range(len(graph))]
    heap = [(0, start)]
    while heap:
        cost, node = heapq.heappop(heap)
        if dist[node] <= cost: continue
        dist[node] = cost
        for i, edge_val in enumerate(graph[node]):
            heapq.heappush(heap, (cost + edge_val, i))

    return dist
```

测试数据(见Python算法书P250)：
```python
F = float('inf')
graph = [
    [0, F, 5, 2, F, F, F],
    [11, 0, 4, F, F, 4, F],
    [F, 3, 0, F, 2, 7, F],
    [F, F, F, 0, 6, F, F],
    [F, F, F, F, 0, F, 2],
    [F, F, F, F, F, 0, 3],
    [F, F, F, F, F, F, 0]
]
print(dijkstra(graph, 0))
```

### 二维地图中的Dijkstra
另外算法题中可能不会那么直白的给出图的结构，通常会给出的是一个二维地图。

下面是我自己出的一个题（参考`LC.505`），可以用Dijkstra算法做。
给出一个迷宫如
```text
0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0
```
和起点`(0, 4)`和终点`(4, 4)`。迷宫中1是障碍物。求起点到终点的最短路径。

下面是代码：
```python
def dijkstra(maze, start, end):
    m, n = len(maze), len(maze[0])
    dist = [[float('inf') for _ in range(n)] for _ in range(m)]
    direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = [(0, start[0], start[1])]
    while heap:
        d, x, y = heapq.heappop(heap)
        if dist[x][y] <= d: continue
        dist[x][y] = d
        for d0, d1 in direcs:
            nx, ny, nd = x+d0, y+d1, d+1
            if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                if end == [nx, ny]: return nd
                heapq.heappush(heap, (nd, nx, ny))
    return -1
```

## 分析
对于图`G = (V, E)`。

时间复杂度方面，
创建结果容器等准备阶段的工作是`O(V)`的。
而主体循环阶段是`O(ElogE)`的。
所以整体时间复杂度在`O(V + ElogE)`左右。

空间复杂度自然是`O(E + V)`。堆中保存E条边，结果容器dist中保存V个节点的信息。