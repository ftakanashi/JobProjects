## 题目描述
在一个有向图中，节点分别标记为 0, 1, ..., n-1。图中每条边为红色或者蓝色，且存在自环或平行边。

red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的蓝色有向边。

返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。

示例 1：
```
输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
输出：[0,1,-1]
```
示例 2：
```
输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
输出：[0,1,-1]
```
示例 3：
```
输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
输出：[0,-1,-1]
```
示例 4：
```
输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
输出：[0,1,2]
```
示例 5：
```
输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
输出：[0,1,1]
```

提示：
```
1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n
```

### 解法 BFS
简单的单源最短路径的一个小变体。
这里不使用Dijkstra等略复杂的算法，而是直接BFS上。

注意题目条件，图是有向图，另外题目也没有对路径的第一条边的颜色做出要求。也就是说到达某个点的合法路径可能是`红蓝红蓝...`或者`蓝红蓝红...`。都可以。

首先建图，由于边存在红色和蓝色的区别，所以我们可以用两个列表分别保存一个节点出发的红色边和蓝色边，这个不难。

然后在BFS时，由于要时刻知道上一步走的边的颜色（才能做到交替颜色），所以BFS过程中需要维护节点、上一条边的颜色、距离三个要素。
由于可以是红边起始或者蓝边起始，因此初始状态下会有两个节点是0的状态。

具体的，我们使用`(node, color, dist)`元组作为队列元素。`color`的0表示红边，1表示蓝边。

另外因为图中可能有环，因此需要加`seen`。但是其中并不能只是单纯一个节点作为不走重复路的标志。
考虑这样一种情况：
某个节点的入边只有一个红色边，也有一个出边指向目标节点。
而此时还有一条蓝色出边指向另一个节点，走这条路可以通过一个环路最终通过一条蓝色入边重新回到本节点，此时可以走向目标节点。
换言之，走重复路的标志应该是 节点 + 走到节点的边的颜色。

在综合考虑上述所有因素后写代码，便可得到正确的代码。