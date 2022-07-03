## 题目描述
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和 达到或超过  100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家 不能 重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定两个整数 maxChoosableInteger （整数池中可选择的最大数）和 desiredTotal（累计和），
若先出手的玩家是否能稳赢则返回 true ，否则返回 false 。假设两位玩家游戏时都表现 最佳 。

示例 1：
```
输入：maxChoosableInteger = 10, desiredTotal = 11
输出：false
解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
```
示例 2:
```
输入：maxChoosableInteger = 10, desiredTotal = 0
输出：true
```
示例 3:
```
输入：maxChoosableInteger = 10, desiredTotal = 1
输出：true
```

提示:
```
1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300
```

### 解法 暴力搜索DFS
这题的解法到没那么多弯弯绕，直接暴力搜索即可。

首先是排除几个状况外的情况。比如`maxChoosableInteger >= desiredTotal`时，先手随便选一个大于等于目标值的数字，就能获胜了，所以直接返回True。
再比如`maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal`时，表示即使两人将所有数字都选完，也没能达到目标值，此时两人都不能获胜，直接返回False。

除此之外就需要搜索了，。
定义DFS函数`dfs(used, total)`，其中参数`used`表示已经使用的数字的集合，`total`表示当前已经累加到的数目。
返回一个bool变量，表示当某个玩家开始选择数字时，碰到的`used, total`这样的情况时，能否保证他必胜。

函数体内，我们遍历`range(1, maxChoosableInteger + 1)`。
针对数字`num`，首先判断其是否在`used`中，若是则跳过。
接着判断是否有`total + num`达到目标值，若是则可以直接返回True。

再接着，就需要进行`dfs(used.add(num), total + num)`的计算了。
注意此时玩家换手，所以此时这个函数必须返回False时，才能保证刚才那个`dfs(used, total)`的玩家必胜。
所以，最关键的那个条件是`if total + num >= desiredTotal or not dfs(used.add(num), total + num)`，才可以返回True。

考虑到可选数字并不多，所以可以用位图代替哈希集。这样dfs还能上记忆化。

值得一提的是，最开始我考虑将player这个参数也放入dfs函数，但是逻辑有点难写…
倒不如官方答案中不引入的来的清晰。
这类博弈的问题用dfs做的时候，看来都是不引入player参数更好一点。