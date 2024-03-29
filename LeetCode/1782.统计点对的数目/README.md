## 题目描述
给你一个无向图，无向图由整数 n  ，表示图中节点的数目，和 edges 组成，其中 edges[i] = [ui, vi] 表示 ui 和 vi 之间有一条无向边。同时给你一个代表查询的整数数组 queries 。

第 j 个查询的答案是满足如下条件的点对 (a, b) 的数目：

a < b
cnt 是与 a 或者 b 相连的边的数目，且 cnt 严格大于 queries[j] 。
请你返回一个数组 answers ，其中 answers.length == queries.length 且 answers[j] 是第 j 个查询的答案。

请注意，图中可能会有 重复边 。

示例 1：

![](https://pic.leetcode-cn.com/1614828447-GMnLVg-image.png)
```
输入：n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
输出：[6,5]
解释：每个点对中，与至少一个点相连的边的数目如上图所示。
```
示例 2：
```
输入：n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
输出：[10,10,9,8,6]
```

提示：
```
2 <= n <= 2 * 104
1 <= edges.length <= 105
1 <= ui, vi <= n
ui != vi
1 <= queries.length <= 20
0 <= queries[j] < edges.length
```

### 解法 二分查找
什么狗屎翻译…我来解读一下题意。

有一个无向图，且图中的两个节点间可以有不止一条边。
任意两个节点可以形成一个点对。一个点对有一个"特征值"，就是这两个点连着的边的总数（当然，两个点之间的边只会被计算一次）。
现在给出一个查询值`query`，要求找出，图中所有"特征值"严格大于`query`的点对的数目。
而`queries`则是多个平行的`query`，互相之间独立求解即可。

这题麻烦的点还挺多。
首先来思考，针对两个点如何计算"特征值"。显然可以先构建图，然后计算两个点的度数的和。
而当两个点之间有直接连线的时候，还得找出这些之间连线的数目，从和中减去，以避免重复计算。

接着，针对`query`，如何计算符合要求的点对数目呢。
直接O(n^2)地遍历所有点对是会超时的。这里我们借鉴官答的做法，将所有节点和对应的度数整理出来之后进行排序。
然后扫描所有点，在固定一个点`a`（以及他的度数`degree_a`）的前提下。
接着我们只需在有序数组中寻找点`b`使得`degree_b > query - degree_a`即可。这显然可以用二分查找来做。

当然考虑到上面说过的重复边的情况，如此得到的答案还不一定是准确的。
但是在扫描过程中控制扣减重复边有点麻烦。
我们可以等扫描全部完成后，再从得到的总值中，减去那些点对`a, b`，which满足`degree_a + degree_b > query`且`degree_a + degree_b - edge(a, b) <= query`
的点对数目即可。

后者的`edge(a, b)`表示两点间直接相邻的边数。
这部分数据也可以在预处理的时候就全部算出来。

大体的框架就是上面这样了， 更多细节我也不知道该以什么逻辑讲，反正就是抄的官答…
更多细节看代码注释吧。