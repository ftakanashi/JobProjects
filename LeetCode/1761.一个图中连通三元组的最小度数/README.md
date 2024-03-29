## 题目描述
给你一个无向图，整数 n 表示图中节点的数目，edges 数组表示图中的边，其中 edges[i] = [ui, vi] ，表示 ui 和 vi 之间有一条无向边。

一个 连通三元组 指的是 三个 节点组成的集合且这三个点之间 两两 有边。

连通三元组的度数 是所有满足此条件的边的数目：一个顶点在这个三元组内，而另一个顶点不在这个三元组内。

请你返回所有连通三元组中度数的 最小值 ，如果图中没有连通三元组，那么返回 -1 。

示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/02/14/trios1.png)
```
输入：n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
输出：3
解释：只有一个三元组 [1,2,3] 。构成度数的边在上图中已被加粗。
```
示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/02/14/trios2.png)
```
输入：n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
输出：0
解释：有 3 个三元组：
1) [1,4,3]，度数为 0 。
2) [2,5,6]，度数为 2 。
3) [5,6,7]，度数为 2 。
```

提示：
```
2 <= n <= 400
edges[i].length == 2
1 <= edges.length <= n * (n-1) / 2
1 <= ui, vi <= n
ui != vi
图中没有重复的边。
```

### 解法 模拟
这题的题意首先稍微绕了几个弯，需要稍微整理一下。
首先是明确是一张无向图。然后，所谓的一个三元组，就是三个节点，两两之间都有一条边相连，形成一个三角形的样式。
而每个这样的三元组，都会有一个属性姑且称之为"三元组的度数"。
定义为，这三个节点的周边的所有边除去两两相连的那些。

而题目要求的，是所有三元组中，"三元组度数"最小的值。

至于做法，虽然这题标了hard，但是实际上却可以直接暴力做。

在构建完图之后，我们遍历所有可能的三元组。
第一步先判断是否有三个节点两两之间互相相连。
如果是就记录这个三元组的"三元组度数"。计算方法也很简单，可以将三个节点的总度数值相加。
得到的和再减去两两相连的边（注意如果使用邻接表构建图，由于边的无向性，每一条边要算两次，也就是最终要减去6

遍历完所有可能的三元组，并且计算得到全局三元组度数的最小值就可以了。

当然以上做法是很明显的 O(n^3)，虽然能AC，不过很不优雅。
官答给出了一种将图改造为有向图的优化方法，可以去看一下，这里就不多说了。