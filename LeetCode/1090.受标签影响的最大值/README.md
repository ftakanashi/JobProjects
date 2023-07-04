## 题目描述
我们有一个 n 项的集合。给出两个整数数组 values 和 labels ，第 i 个元素的值和标签分别是 values[i] 和 labels[i]。还会给出两个整数 numWanted 和 useLimit 。

从 n 个元素中选择一个子集 s :

子集 s 的大小 小于或等于 numWanted 。
s 中 最多 有相同标签的 useLimit 项。
一个子集的 分数 是该子集的值之和。

返回子集 s 的最大 分数 。

示例 1：
```
输入：values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
输出：9
解释：选出的子集是第一项，第三项和第五项。
```
示例 2：
```
输入：values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
输出：12
解释：选出的子集是第一项，第二项和第三项。
```
示例 3：
```
输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
输出：16
解释：选出的子集是第一项和第四项。
```

提示：
```
n == values.length == labels.length
1 <= n <= 2 * 104
0 <= values[i], labels[i] <= 2 * 104
1 <= numWanted, useLimit <= n
```

### 解法 贪心 哈希表 排序
乍一看还以为要当成背包问题来做，但实际上没有那么复杂，有更朴素的办法。

注意到，`useLimit`是一个比较关键的指标。表示同标签的物品最多只能选`useLimit`个。
因此，我们可以遍历所有物品，并且把所有相同标签的物品归类，同时只需要维护同标签中最多`useLimit`个，即value是max的`useLimit`个。

在有了这些物品后，由于`numWanted`的定值是独立的，所以可能会比这些所有物品加起来的数量更多或者更少。
更少或者相等的情况，则需要将这些物品全部拿出来根据value进行排序，取前`numWanted`个即可。
否则这些物品可以全取。

更多细节详情见代码。（可能写的比较ugly，懒得优化了。