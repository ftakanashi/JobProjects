## 题目描述
给你一个 n 个点组成的无向图边集 edgeList ，其中 edgeList[i] = [ui, vi, disi] 表示点 ui 和点 vi 之间有一条长度为 disi 的边。请注意，两个点之间可能有 超过一条边 。

给你一个查询数组queries ，其中 queries[j] = [pj, qj, limitj] ，你的任务是对于每个查询 queries[j] ，判断是否存在从 pj 到 qj 的路径，且这条路径上的每一条边都 严格小于 limitj 。

请你返回一个 布尔数组 answer ，其中 answer.length == queries.length ，当 queries[j] 的查询结果为 true 时， answer 第 j 个值为 true ，否则为 false 。

示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/12/19/h.png)
```
输入：n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
输出：[false,true]
解释：上图为给定的输入数据。注意到 0 和 1 之间有两条重边，分别为 2 和 16 。
对于第一个查询，0 和 1 之间没有小于 2 的边，所以我们返回 false 。
对于第二个查询，有一条路径（0 -> 1 -> 2）两条边都小于 5 ，所以这个查询我们返回 true 。
```

示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/12/19/q.png)
```
输入：n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
输出：[true,false]
解释：上图为给定数据。
```

提示：
```
2 <= n <= 105
1 <= edgeList.length, queries.length <= 105
edgeList[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 109
两个点之间可能有 多条 边。
```

### 解法 并查集 离线查询
一道比较典型，但是又没那么典型的并查集题目。

在以往的经验中，我总是下意识地认为，所有并查集的使用都是整理完整个图的结构之后，先"充值"所有边，然后再"使用"边。
但是这题如果按照这种思想，就会有一个很麻烦的事情，就是面对一个query中的limit，我不知道之前充值进的边是否保证符合要求。

这里就需要稍微灵活一点了。

具体的，我们在充值边之前先对所有edgeList做一个基于边长的排序。由于答案的顺序之和queries的顺序有关。所以这个排序是无所谓的。
然后面对一个query比如`(x, y, limit)`，我们可以想象，只要将所有边权值小于`limit`的边充值进去，而其他的都暂时不充，
在此时间点上，我们就可以通过并查集来判断`x`和`y`之间是否有合法的路径了。

现在更加麻烦一点的是会有多个query。我们不能每一个query就从头充值一次边。所以我们可以事先记住query的顺序的前提下，对query也做一次基于limit的排序。

总的来说，我们先从小到大遍历query，并且维护一个指向edgeList中元素的指针。
碰到`(x, y, limit)`这样一个query的时候，就将所有边长小于`limit`的所有edgeList中的边都加入并查集。

注意，这个过程在整个遍历过程中是累积的，因此我们可以保证所有符合要求的边都会被考虑。

这里顺便推一个极简版的并查集模板代码：
```python
n = 10    # 总节点数
fa = [i for i in range(n)]

def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

def merge(x, y):
    fa[find(x)] = find(y)
```

剩下的就看代码吧。