## 题目结束
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。

一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。

例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
>输入：m = 2, n = 3, k = 1
>
>输出：3

示例 2：
>输入：m = 3, n = 1, k = 0
>
>输出：1

提示：

- 1 <= n,m <= 100
- 0 <= k <= 20

### 解法1 DFS
这题和前面第十二题几乎一样。都是DFS探索。
其实想得简单一点，创建一个地图然后把不符合题目要求的格子涂黑成障碍物的话，这就是一个简单的走迷宫问题。

由于要求的是所有能够到达的格子的计数，所以我的办法是，维护一个visited矩阵，初始化为0，每有一个可以到达的格子，
就置为1。

当所有DFS完成之后，把visited矩阵整个求和即可。

整体代码框架真的和JZ12几乎一模一样，而且细节更简单一些。因为这里DFS不用返回什么东西，只需要"没路走了就停止探索"即可。

### 解法2 BFS
待补充