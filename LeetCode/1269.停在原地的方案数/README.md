## 题目描述
有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。

每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。

给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。

由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。

示例 1：
```
输入：steps = 3, arrLen = 2
输出：4
解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
向右，向左，不动
不动，向右，向左
向右，不动，向左
不动，不动，不动
```
示例  2：
```
输入：steps = 2, arrLen = 4
输出：2
解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
向右，向左
不动，不动
```
示例 3：
```
输入：steps = 4, arrLen = 2
输出：8
```

提示：
```
1 <= steps <= 500
1 <= arrLen <= 10^6
```

### 解法 DP
难得碰到一道标着"困难"但是觉得不困难的题目。

一看就知道用DP。写一下也立刻想到了DP数组应该是`steps * arrLen`的矩阵。
`dp[i][j]`表示走第`i`步后处于位置`j`的方案总数。

为了方便，可以将`steps`维度+1，包括走0步的初始情况。
接下来，状态转移方程也很简单：
```python
dp[i][j] = sum(dp[i-1][j-1:j+2])    # 当然别忘了判断边界情况
```
最后返回`dp[-1][0]`即可得到答案。

上述是最朴素的DP。
接下来看能不能优化。注意到，状态转移方程中，`dp[i][j]`之和`dp[i-1]`中的几个状态相关。
由于前后都有相关，不能通过一个方向的递推压缩空间，因此可以考虑整两个DP一维数组，进行数组轮换的方式来实现空间的压缩。

此外，题目给出的限制，steps是小于等于500，而arrLen可能会很大。导致DP矩阵会很宽。
同时，矩阵右上角那一部分会有大量的0，因为在第`i`行，最远只能走到`i`列，如果`j>>i`，就会出现大量冗余0。
所以我们发现，没必要维护长度为arrLen的完整的DP数组。
只需要维护其有效部分，即前`i`个元素即可。
具体的，当走第`i`步的时候，如果当前dp数组长度仍然小于arrLen，那么就append上一个0，再做DP状态递推操作。

最后别忘了大数要`% 10**9+7`。