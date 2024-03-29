## 题目描述
给你一个整数 n ，表示有 n 节课，课程编号从 1 到 n 。同时给你一个二维整数数组 relations ，其中 relations[j] = [prevCoursej, nextCoursej] ，表示课程 prevCoursej 必须在课程 nextCoursej 之前 完成（先修课的关系）。同时给你一个下标从 0 开始的整数数组 time ，其中 time[i] 表示完成第 (i+1) 门课程需要花费的 月份 数。

请你根据以下规则算出完成所有课程所需要的 最少 月份数：

如果一门课的所有先修课都已经完成，你可以在 任意 时间开始这门课程。
你可以 同时 上 任意门课程 。
请你返回完成所有课程所需要的 最少 月份数。

注意：测试数据保证一定可以完成所有课程（也就是先修课的关系构成一个有向无环图）。

示例 1:

![](https://assets.leetcode.com/uploads/2021/10/07/ex1.png)
```
输入：n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
输出：8
解释：上图展示了输入数据所表示的先修关系图，以及完成每门课程需要花费的时间。
你可以在月份 0 同时开始课程 1 和 2 。
课程 1 花费 3 个月，课程 2 花费 2 个月。
所以，最早开始课程 3 的时间是月份 3 ，完成所有课程所需时间为 3 + 5 = 8 个月。
```
示例 2：

![](https://assets.leetcode.com/uploads/2021/10/07/ex2.png)
```
输入：n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]
输出：12
解释：上图展示了输入数据所表示的先修关系图，以及完成每门课程需要花费的时间。
你可以在月份 0 同时开始课程 1 ，2 和 3 。
在月份 1，2 和 3 分别完成这三门课程。
课程 4 需在课程 3 之后开始，也就是 3 个月后。课程 4 在 3 + 4 = 7 月完成。
课程 5 需在课程 1，2，3 和 4 之后开始，也就是在 max(1,2,3,7) = 7 月开始。
所以完成所有课程所需的最少时间为 7 + 5 = 12 个月。
```

提示：
```
1 <= n <= 5 * 104
0 <= relations.length <= min(n * (n - 1) / 2, 5 * 104)
relations[j].length == 2
1 <= prevCoursej, nextCoursej <= n
prevCoursej != nextCoursej
所有的先修课程对 [prevCoursej, nextCoursej] 都是 互不相同 的。
time.length == n
1 <= time[i] <= 104
先修课程图是一个有向无环图。
```

### 解法 记忆化DFS
这题是属于比较简单的hard题，而且代码量也不多，主要还是要理清思路。

为了方便，我们可以将前序课程定义为上方，后续课程定义为下方，那么整个图是一个有层级的。
而最上层的那些课，根据题意，我们可以同时开始学，并且完成某个后续课程的所有前序课程之后，就可以进入下一层的后序课程学习。

基于这样一个情况，我们可以设计一个dfs函数，`dfs(node)`返回值用来表示学完编号为`node`的课程需要的最少时间。

显然，对于所有最上层的入口课程，`dfs(node)`是`time[node - 1]`（别忘了`node`不是下标是编号
而对于所有非最上层的课程，直接的思路就是扫描其所有前序课程，获得到那些课程完成的最少时间中的最大值。
这个值是可以开始本课程学习的最早时间点，再在这个基础上加上本课程需要的时间，就得到了本课程dfs的返回值。

显然，这是一个dfs递归过程。同时因为可能同一门上层课程是多门下层课程的前序课程，所以可以为dfs函数加上记忆化从而加快搜索时间。

在dfs外部，由于题目中的所有课程编号都有可能是最底层的课程，因此可以遍历一遍所有的`node`。
因为有记忆化，不用担心重复计算。