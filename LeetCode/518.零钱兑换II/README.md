## 题目描述
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

示例 1:
```
输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```
示例 2:
```
输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
```
示例 3:
```
输入: amount = 10, coins = [10] 
输出: 1
```

注意:
你可以假设：
```
0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数
```

### 解法 DP（完全背包问题）
联动`LC.322`。
首先，一眼就可以看出这是一个完全背包问题。
由于是个求方案数的问题，按照套路，首先定义出DP数组
`dp[i][j]`表示使用前`i`种硬币时，可以得到目标值`j`的方案数目。并初始化`dp[0][0] = 1`。

接着扫描填充DP数组。显然，当`j - coins[i-1] >= 0`时，说明当前硬币种类可取，根据求方案数的转移方程模板以及这是个完全背包问题，
写出转移方程如下：
```python
if j - coins[i-1] >= 0:
    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
else:
    dp[i][j] = dp[i-1][j]
```
老规矩，非状态压缩的代码写在注释里，而实际跑的是压缩后的代码。

这个问题可以说也是一个经典的 求方案数的背包问题。