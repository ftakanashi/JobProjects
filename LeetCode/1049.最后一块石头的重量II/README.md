## 题目描述
有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

- 如果 x == y，那么两块石头都会被完全粉碎；
- 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。

最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。

示例 1：
```
输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
```
示例 2：
```
输入：stones = [31,26,33,21,40]
输出：5
```
示例 3：
```
输入：stones = [1,2]
输出：1
```

提示：
```
1 <= stones.length <= 30
1 <= stones[i] <= 100
```

### 解法 DP （背包问题）
这道题其实和`LC.494`的DP解法很像。
乍一看题情比较复杂，但是如果能够意识到这其实是个背包问题的话，解法本身就是经典的01背包，没有任何难度。

首先我们要意识到，所谓的挑两块石头互相砸直到最后的过程，其实就是给所有数字前面附上加号或者减号，然后求最后和的过程。

当然，这里附加号或减号是有一定限制的，最显而易见的，我不能全部附加号也不能全部附减号。
思考后发现，由于选取石头的顺序没有任何要求，所以只要附上加减号之后最终的和非负，就说明这组加减号就表示了一种可行的方案。
（详细证明见官方题解）

于是，我们将所有附减号的数字的和表示为`neg`，整个数组的所有和表示为`sum`，显然，剩余附加号的和是`sum-neg`。
另一方面，模拟计算最后一块石头的重量，即附上加减号后数组的和可以表示为`sum - neg - neg`，即
`sum - 2*neg`。

上面这个值要非负但尽量小，换句话说，就是`neg`需要满足`neg <= sum/2`且要尽量大。

显然，这就是一个 重量和价值都为`stones[i]`的物品，背包容量是`sum / 2`的01背包问题了。

更细节的，其实容量是`sum // 2`。当sum不能整除的时候，显然应该向下取整保证结果的非负。

至于01背包问题怎么做就不多说了，简单了。
最后别忘了，DP数组最后获得的值是`neg`，而要求的是`sum - 2*neg`。