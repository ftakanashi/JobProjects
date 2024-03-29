## 题目描述
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

示例 1：
```
输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
```
示例 2：
```
输入：triangle = [[-10]]
输出：-10
```

提示：
```
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
```

进阶：
```
你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
```

### 解法 空间优化DP
乍一看，这题感觉和遍历树或者二维地图挺像的，就梭一把DFS试试，结果最后一个case超时…

于是改用DP。
最开始，显然定义DP数组为`dp[n][n]`，`dp[i][j]`表示走到`triangle[i][j]`位置时路径和的最小值。
这里还提醒注意一下，虽然是个三角形，但是还是以二维坐标来理解会更加方便。
于是轻易得出递推方程：
```python
dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
```
为了避免`j == 0`时`j-1 < 0`的出现，事先将所有`dp[i][0]`用前缀和技巧填充好。

接着看题目说要O(n)空间，而上述递推方程也确实只和`i-1`行信息相关，于是二维DP转一维。
因为是和`j-1`相关，所以内层循环要从右往左扫描。
此外一维化之后，因为无法提前将所有最左边的值填充好，因此`j-1 < 0`的情况无法避免。
此时干脆将`dp[0]`的情况单独拿到内层循环外面做。
以上。