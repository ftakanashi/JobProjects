##题目描述
（题目中有比较多图，懒得copy了，可以看原网页）

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：
>输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
>
>输出：2
>
>解释：
>
>3x3 网格的正中间有一个障碍物。
>
>从左上角到右下角一共有 2 条不同的路径：
>
>1. 向右 -> 向右 -> 向下 -> 向下
>
>2. 向下 -> 向下 -> 向右 -> 向右

示例 2：
>输入：obstacleGrid = [[0,1],[0,0]]
>
>输出：1
 

提示：
- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] 为 0 或 1

### 解法1 DP
这个题就是非常非常典型的，既可以DP又可以DFS的题目。先说DP。
基本思路和LC.62一模一样，无非就是加个地图上是否是障碍物的判断而已。

另外注意一点，初始化dp矩阵的时候，原本可以简单的将第一行第一列全置1。

但是这题的情况，由于只允许向下和向右走，所以对于第一行某个位置出现障碍物之后，后面所有位置都应该是0，即无法到达。第一列同理。

### 解法2 带记忆的DFS
单纯的DFS会超时。因此需要加入记忆机制。

一开始我设计的dfs函数是在内部使全局变量`count += 1`，到达终点后直接返回。
这样的话dfs函数体中很难有地方插入对于记忆的写入操作。

转变思路，dfs变成返回某个点出发到达终点的路径种数。
显然终点直接返回1即可。其余点，则是其右边点和下面点结果的和。

这样在返回前就可以直接写入mem。