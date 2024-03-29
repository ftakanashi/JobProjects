## 题目描述

给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:
```
输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
```
示例 2:
```
输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
```

### 解法 DP
和`LC300`很像。

一开始，使用LC300的思路思考这道题，比如`1 3 5 4 7`这个例子，得到的dp数组值是`1 2 3 3 4`。
最大值是4。

而这个4其实是可以通过两种 3 + 1 得到，这也是最后答案2的出处。

如何根据得到的最长长度4找出可以得到这种最长长度的路径成为关键问题。

其实可以发现，当以`7`作为基准，扫描前面所有数时，扫过`5`之后，`7`的dp值已经变成4。
而后面扫描`4`时其dp值+1恰好也是当前`7`的dp值4，因此产生了两种"路径"。

所以考虑除了记录长度的dp数组之外，再开一个记录当前位置为右边界时能够达到最长长度的路径种类数。

假设两个数组分别为`dp_len`和`dp_con`的话。
那么针对`dp_con`其实有如下状态转移方程：
```text
if dp_len[i] < dp_len[j] + 1:
    dp_con[i] = dp_con[j]
    dp_len[i] = dp_len[j] + 1    # 别忘了dp_len的更新
elif dp_len[i] == dp_len[j] + 1:
    dp_con[i] += dp_con[j]
```

以两个dp数组进行dp扫描，最后得到两个数组后，将`dp_len`中最长长度的位置找出来，并将这些位置对应的`dp_con`给加和起来，问题就解决了。