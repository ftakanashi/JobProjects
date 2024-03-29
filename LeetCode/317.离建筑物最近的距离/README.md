## 题目描述
你是个房地产开发商，想要选择一片空地 建一栋大楼。你想把这栋大楼够造在一个距离周边设施都比较方便的地方，通过调研，你希望从它出发能在 最短的距离和 内抵达周边全部的建筑物。请你计算出这个最佳的选址到周边全部建筑物的 最短距离和。

提示：
- 你只能通过向上、下、左、右四个方向上移动。

给你一个由 0、1 和 2 组成的二维网格，其中：
- 0 代表你可以自由通过和选择建造的空地
- 1 代表你无法通行的建筑物
- 2 代表你无法通行的障碍物

示例：
```
输入：[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
输出：7 
解析：
给定三个建筑物 (0,0)、(0,4) 和 (2,2) 以及一个位于 (0,2) 的障碍物。
由于总距离之和 3+3+1=7 最优，所以位置 (1,2) 是符合要求的最优地点，故返回7。
```

注意：
```
题目数据保证至少存在一栋建筑物，如果无法按照上述规则返回建房地点，则请你返回 -1。
```

### 解法 BFS
这题乍一看，就知道得用BFS。然而细节上还是有很多需要注意的地方，我们一点点来看。

首先，因为针对每个空地都要求出到所有建筑物的距离，换句话说，靠多源BFS多起点出发遍历一次全图就好了那种事情没有了。
因为要求总距离，很自然的，想到了维护一个空地到所有建筑物的距离和的矩阵（这个矩阵与地图同size），然后从不同建筑物出发BFS，探索到这个空地时可以知道
该建筑物到该空地的最短距离，然后再在距离和矩阵的这个空地位置上，累加上这个最短距离即可。

但是仅仅这样还是不够的。注意到这样一个问题：某些空地或者建筑物，可能会被障碍物包围。
若被包围的是建筑物，则说明全局没有一块空地可行，应该返回-1。
若被包围的是空地，这块空地在结束所有探索后其距离和数组中的值必然是0，但是这个0可不能作为最终答案。

为了解决上面问题，我们还需要一个机制统计某块空地是不是可以到达所有建筑物。
为此，额外再开一个可到达建筑物总计的矩阵（也是同地图size）。
从建筑物出发，BFS探索到某个空地时，不但要将探索距离累加到距离和矩阵上，还要将可达建筑物统计矩阵相应位置加1。

这样，探索全部完成后，只需要检查满足下列要求的位置：
- 原地图中是空地
- 可达建筑物统计矩阵中的值等于建筑物总个数
将所有符合要求位置的距离和矩阵中的值的min返回出来作为最终答案。