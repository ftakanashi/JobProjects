## 题目描述
我们将给定的数组 A 分成 K 个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。

注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。

示例:
```
输入: 
A = [9,1,2,3,9]
K = 3
输出: 20
解释: 
A 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
我们也可以把 A 分成[9, 1], [2], [3, 9].
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
```
说明:
```
1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
答案误差在 10^-6 内被视为是正确的。
```

### 解法 DP + 前缀和
一道线性的DP题。
最开始的想法，当然就是建立DP数组`dp[i]`表示前`i`个数分成K组时可以得到的最大分数。
但是在`i > K`的位置上，我们还需要枚举K个子数组分别分割在什么地方，导致很复杂。

于是想到将K这个影响因子也引入DP推导的过程。将DP数组扩展成`dp[i][j]`，表示前`i`个数分成`j`组时能够得到的最大分数。

在这种定义下，为了确定`dp[i][j]`，我们可以遍历所有小于`i`的位置`x`，将`x`作为`j-1`个分组的末尾，于是`x+1`到`i`的数字作为第`j`个分组。
那么状态转移方程就是：
```text
dp[i][j] = max(
    dp[x][j-1] + nums[x+1]到nums[i]之间子数组的平均值
)
```
问题就变成了，上述式子后半平均值怎么求。
显然这种和子数组和、子数组平均值相关的问题，用前缀和就完事了。
维护一个标准的前缀和数组，那么上面这个值就是`(presum[i+1] - presum[x+1]) / (i - x)`。
(注意标准前缀和开头有个额外的零，所以下标都要+1)

另外还要注意，如果`i` < `j`，那么`i`个数不可能能分出`j`个组来，所以直接置零即可。

最后只剩下初始化的问题了。显然，第一列是所有数只分一组的情况，因此有`dp[i][0] = presum[i+1] / (i+1)`。

按照以上思路写代码即可。
注意遍历dp数组本身需要`O(n*k)`的时间。另外在每个位置，还需要遍历前一个分组末尾的元素，额外乘O(n)时间。
所以总体是`O(n^2 * k)`。

以上做法没有引入额外的dummy行列，所以前缀和下标和dp下标差一个1，写代码的时候要注意细节上别出错。