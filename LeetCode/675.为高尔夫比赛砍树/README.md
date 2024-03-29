## 题目描述
你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中：

- 0 表示障碍，无法触碰
- 1 表示地面，可以行走
- 比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度

每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。

你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。

你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。

可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。

示例 1：

![](https://assets.leetcode.com/uploads/2020/11/26/trees1.jpg)
```
输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
输出：6
解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。
```
示例 2：

![](https://assets.leetcode.com/uploads/2020/11/26/trees2.jpg)
```
输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
输出：-1
解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。
```
示例 3：
```
输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
输出：6
解释：可以按与示例 1 相同的路径来砍掉所有的树。
(0,0) 位置的树，可以直接砍去，不用算步数。
```

提示：
```
m == forest.length
n == forest[i].length
1 <= m, n <= 50
0 <= forest[i][j] <= 109
```

### 解法 暴力BFS
这题之所以被标成hard，估计是因为有可以用A\*之类的高级算法做的缘故。
如果不追求这么高级的做法的话，那么暴力BFS足矣，并且思路和代码实现都不复杂。

首先分析题意，1是地面，0是障碍物。要求从2开始从小到大按顺序砍树。
值得注意的是，一个格子里的树即使没被砍倒这个格子依然可以走过。

于是题目其实就变成了，求高度是2的树的格子走到高度是3的树的格子的最短路径，
加上从高度是3的格子走到高度是4的格子的最短路径，加上……以此类推。

这个显然每个子问题用BFS做很方便。
于是定义一个`bfs(start, end)`表示从start点走到end点的最短路径。
然后按照上面的逻辑分别求就是了。
注意中途一旦某两个点之间的路径求出是-1，就说明了这两个点不通，说明整体不存在符合要求的方案。
所以直接返回-1即可。