## 题目描述
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
```
"123"
"132"
"213"
"231"
"312"
"321"
```
给定 n 和 k，返回第 k 个排列。

示例 1：
```
输入：n = 3, k = 3
输出："213"
```
示例 2：
```
输入：n = 4, k = 9
输出："2314"
```
示例 3：
```
输入：n = 3, k = 1
输出："123"
```

提示：
- 1 <= n <= 9
- 1 <= k <= n!

### 解法 按规律确定各位数字，递归
看到这题第一想法是DFS按照顺序不断探索排列，然后计数，直到计数到达k。

但是试了下发现超时。于是换思路。

有几个显而易见的事实：
首先答案的各个位置数字一定是从`range(1,n+1)`之间选的。
而从左到右每一位数字其实在k值给出之后就可以确定了。

以`n=9`为例，第一位数字是什么？其实看k值。如果k是在`[1, 8!]`的闭区间范围内，那么第一位一定是1；
类似的，如果k在`[8!+1, 8!*2]`，那么第一位就是2。以此类推。

确定了第一位之后第二位如何确定？显然，k减去所在的那个区间的lower bound，其实就是说我是这个区间的第几个数字。
而这其实成为了一个更小规模的问题，即可选数字范围是`range(1, n+1).remove(第一位数字)`，而`new_k = k - lower bound`。

这么一来，显然，递归走起。
由于最开始候选数字序列`candidates = range(1, n+1)`是有序的，所以在确定数字过程中不断remove掉一些数字，也不会破坏其有序性。
因此每一层递归的条件是一致的。

递归结束的条件有很多种写法，给出的代码中我用的是查看candidates剩余数字量，如果只剩下一个，那么直接将其加入res后返回即可。

否则，先计算当前candidates长度-1的阶乘。这个作为一个base，循环，不断加大其倍数，看k在什么时候小于了`i + 1`倍的base。

这里故意写成i+1是为了方便后续直接拿到需要用的数字在candidates中的下标i。

然后别忘了，k还要减去lower bound，这里是i倍的base。然后开始下一轮递归即可。