## 题目描述
给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi] 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。

所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。

例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。
假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。

示例 1：
![](https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg)
```
输入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
输出：["JFK","MUC","LHR","SFO","SJC"]
```
示例 2：

![](https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg)
```
输入：tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。
```

提示：
```
1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi 和 toi 由大写英文字母组成
fromi != toi
```

### 解法1 回溯DFS
题目意思挺好懂的。
关键在于，如何保证最终路径的字典序最小。
换言之，如果没有要求字典序最小这个条件，那么这个题其实就是一个简单的给你一个图，然后求出一个可以遍历到所有点的路径的问题。
并且题目还规定了，起始点一定是JFK。
上述问题，可以通过回溯的DFS来做。

通常回溯DFS遍历图的时候，对于到达某个节点后，继续通过哪个边前往下一个节点没有固定要求，都是无序遍历的。
现在既然要求字典序最小，显然我们就应该优先考虑能够使得字典序最小的边作为优先选项。
当走这条边走不通时，再去考虑字典序更大的边（贪心思想）。

于是就没有什么难度了。无非就是在对下一条边进行选择时进行一个排序。
这个排序工作也可以在dfs开始前，直接在构建临接表的时候就完成。

因为题目要求所有票都要被用到，所以dfs函数的终结时机需要斟酌一下。
具体来说，可以在dfs函数中维护一个当前还有多少票没用到的变量。当进入到某个点时，没有下一个行程可走，而恰好这个数值归零，那么认为当前走过的行程是一个
合法的行程。（注意此时最后一个到达的地点尚未被收割，所以在这里还要被收割一下。
如果无路可走时还有票剩余，说明行程不合法。

注意上述算法中，dfs函数输入是`pos`和`rest`，但是其具体返回什么还需要用外部的图的邻接表来判断，所以这里dfs函数不能加cache记忆化。

### 解法2 欧拉通路的Hierholzer算法
这道题题意，抽象一下，其实和小学奥数中的一笔画问题很像。
即，给出n个节点和m条边，问是否能够一笔画从某个起点出发到达某个终点，期间每条边都恰好被使用一次。
数学上，起点与终点相同的情况，这个路径成为欧拉回路；若起点与终点不相同，则路径成为欧拉通路。

小学奥数中我们知道，当图中无奇度节点时，有欧拉回路；当图中仅有两个奇度节点时，有欧拉通路。
上述是建立在图是无向图的基础上。
在有向图的情况中，当每个节点的入度出度都相等时有欧拉回路；当有两个节点，一个入度比出度大1，一个出度比入度大1，其余节点入出度相同时，有欧拉通路。

以上是理论知识，这题显然是一个有向图中秋是否有欧拉回路/通路的问题。
这个问题可以通过Hierholzer算法求解。

这个算法的大体思想是，我们走图的过程中，要尽量避免走进死胡同。而一个节点当前是否是死胡同，还与之前走过的与之有关的边相关。
这就导致如果自顶向下地去dfs会很复杂。

所以反其道而行之，采用一个栈保存节点路径。从起点开始扫描后，每碰到一个死胡同，就将其入栈。然后返回上层。
因为题目保证了有解，所以全程必然只有一个节点会变成死胡同。
这样就可以自底向上地避免了回溯来做DFS。
这么说可能很难理解，建议直接看代码理解，比较好一点。